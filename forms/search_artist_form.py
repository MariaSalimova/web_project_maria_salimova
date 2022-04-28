from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchArtistForm(FlaskForm):
    username = StringField('Имя художника', validators=[DataRequired()])
    submit = SubmitField('Искать')
