from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    uid = StringField('User', validators=[DataRequired()])
    dat = StringField('Data', validators=[DataRequired()])