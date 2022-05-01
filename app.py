from flask import Flask, render_template, redirect
from data import *
from forms import *
from secret_key import SECRET_KEY
from admin_password import ADMIN_PASSWORD
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
global_init('gallery.db')


@app.route('/')
def main_page():
    return render_template('navigation_page.html', title='Главная страница')


@app.route('/artists/<artist_id>')
def artists_pictures(artist_id):
    db_sess = create_session()
    artist = db_sess.query(Artist).filter(Artist.id == artist_id).first()
    pictures = db_sess.query(Picture).filter(Picture.artist_id == artist_id).all()
    return render_template('artists_pictures.html', artist=artist, pictures=pictures)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Artist).filter(Artist.artist_name == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('generic_form.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = create_session()
        if db_sess.query(Artist).filter(Artist.email == form.email.data).first():
            return render_template('generic_form.html', title='Регистрация',
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
    return render_template('generic_form.html', title='Регистрация', form=form)


@app.route('/add_picture')
@login_required
def add_picture():
    # TODO: здесь будет реализована фича добавления картины
    pass


@app.route('/view_picture/<picture_id>')
def view_picture(picture_id):
    # TODO: здесь будет реализована фича просмотра картины
    pass


@app.route('/search_picture', methods=['GET', 'POST'])
def search_picture():
    form = SearchPictureForm()
    if form.validate_on_submit():
        db_sess = create_session()
        picture = db_sess.query(Picture).filter(Picture.artist == form.artist_name.data,
                                                Picture.title == form.title.data).first()
        return redirect(f'/view_picture/{picture.id}')
    return render_template('search_picture.html', title='Искать картину', form=form)


@app.route('/search_artist', methods=['GET', 'POST'])
def search_artist():
    form = SearchArtistForm()
    if form.validate_on_submit():
        db_sess = create_session()
        artist = db_sess.query(Artist).filter(Artist.artist_name == form.username.data).first()
        print(artist)
        return redirect(f'/artists/{artist.id}')
    return render_template('search_artist.html', title='Искать художника', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/rate_picture')
def rate_picture():
    # TODO: здесь будет реализована фича оценки картины
    pass


@app.route('/delete_picture', methods=['GET', 'POST'])
def delete_picture():
    form = DeletePictureForm()
    if form.validate_on_submit():
        if form.admin_password.data == ADMIN_PASSWORD:
            db_sess = create_session()
            picture = db_sess.query(Picture).filter(Picture.artist == form.artist_name.data,
                                                    Picture.title == form.title.data).first()
            db_sess.delete(picture)
            db_sess.commit()
        return redirect('/')
    return render_template('delete_picture.html', title='Удалить картину', form=form)


@app.route('/delete_artist', methods=['GET', 'POST'])
def delete_artist():
    form = DeleteArtistForm()
    if form.validate_on_submit():
        if form.admin_password.data == ADMIN_PASSWORD:
            db_sess = create_session()
            artist = db_sess.query(Artist).filter(Artist.artist_name == form.username.data).first()
            db_sess.query(Picture).filter(Picture.artist_id == artist.id).delete()
            db_sess.delete(artist)
            db_sess.commit()
        return redirect('/')
    return render_template('delete_artist.html', title='Удалить художника', form=form)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(Artist).get(id)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
