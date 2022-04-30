from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchPictureForm(FlaskForm):
    artist_name = StringField('Имя художника', validators=[DataRequired()])
    title = StringField('Название картины', validators=[DataRequired()])
    submit = SubmitField('Поиск')
