from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DeletePictureForm(FlaskForm):
    artist_name = StringField('Имя художника', validators=[DataRequired()])
    title = StringField('Название картины', validators=[DataRequired()])
    admin_password = StringField('Пароль администратора', validators=[DataRequired()])
    submit = SubmitField('Удалить')
