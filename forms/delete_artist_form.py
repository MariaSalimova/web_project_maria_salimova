from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeleteArtistForm(FlaskForm):
    username = StringField('Имя художника', validators=[DataRequired()])
    admin_password = StringField('Пароль администратора', validators=[DataRequired()])
    submit = SubmitField('Удалить')
