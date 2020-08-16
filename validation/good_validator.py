from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class GoodValidator(FlaskForm):
    name = StringField(label='good_name', validators=[DataRequired()])

