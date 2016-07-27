from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class SearchForm(Form):
    name = StringField('Enter search value', validators=[DataRequired(), Length(min=0)])
    search = SubmitField('Search!')
