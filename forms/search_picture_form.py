from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchPictureForm(FlaskForm):
    title = StringField('Название картины', validators=[DataRequired()])
    submit = SubmitField('Поиск')
