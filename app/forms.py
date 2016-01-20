from flask.ext.wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class EnteredText(Form):
	enteredtext = TextAreaField('enteredtext', validators=[DataRequired()])
