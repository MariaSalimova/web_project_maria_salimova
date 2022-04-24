from flask import Flask, render_template, redirect
from data.db_session import global_init, create_session
from data.artist import Artist
from forms.registration_form import RegisterForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'искусство_должно_быть_свободным'
global_init('gallery.db')


@app.route('/')
def main_page():
    return "искусство должно быть свободным"


@app.route('/<artist_id>')
def pictures_catalog(artist_id):
    pass


@app.route('/login')
def login():
    pass


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


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
