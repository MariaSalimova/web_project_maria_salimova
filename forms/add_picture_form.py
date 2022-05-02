from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired


class AddPictureForm(FlaskForm):
    title = StringField('Название картины', validators=[DataRequired()])
    image = FileField('Картина', validators=[DataRequired()])
    submit = SubmitField('Поиск')
