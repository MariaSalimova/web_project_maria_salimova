from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField
from wtforms.validators import DataRequired


class RatePictureForm(FlaskForm):
    opinion = RadioField('Оценка', choices=['Нравится', 'Не нравится'], validators=[DataRequired()])
    submit = SubmitField('Оценить')
