from flask import Flask, render_template, redirect
from data.db_session import global_init, create_session
from data.artist import Artist
from data.picture import Picture
from forms.registration_form import RegisterForm
from forms.login_form import LoginForm
from forms.search_artist_form import SearchArtistForm
from secret_key import SECRET_KEY
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
global_init('gallery.db')


@app.route('/')
def main_page():
    # TODO: здесь будет реализована фича навигации по сайту
    return "искусство должно быть свободным"


@app.route('/artists/<artist_id>')
def artists_pictures(artist_id):
    # TODO: здесь будет реализована фича просмотра каталога картин
    db_sess = create_session()
    pictures = db_sess.query(Picture).filter(Picture.artist_id == artist_id).all()
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(Artist).filter(Artist.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Artist(
            artist_name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/add_picture')
@login_required
def add_picture():
    # TODO: здесь будет реализована фича добавления картины
    pass


@app.route('/view_picture/<picture_id>')
def view_picture(picture_id):
    # TODO: здесь будет реализована фича просмотра картины
    pass


@app.route('/search_picture')
def search_picture(picture_name):
    # TODO: здесь будет реализована фича поиска картины по названию
    pass


@app.route('/search_artist', methods=['GET', 'POST'])
def search_artist():
    form = SearchArtistForm()
    if form.validate_on_submit():
        db_sess = create_session()
        artist = db_sess.query(Artist).filter(Artist.artist_name == form.username.data).first()
        print(artist)
        return redirect(f'/artists/{artist.id}')
    return render_template('search_artist.html', title='Искать художника', form=form)
    pass


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(id):
    return Artist.get(id)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
