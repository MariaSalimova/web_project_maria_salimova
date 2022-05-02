from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired


class RatePictureForm(FlaskForm):
    artist_name = StringField('Имя художника', validators=[DataRequired()])
    title = StringField('Название картины', validators=[DataRequired()])
    opinion = RadioField('Оценка', choices=['Нравится', 'Не нравится'], validators=[DataRequired()])
    submit = SubmitField('Оценить')
