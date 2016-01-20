from flask import render_template
from app import app
from .forms import EnteredText
from .analysis import NLTKanalysis
import nltk

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = EnteredText()
	if form.validate_on_submit():
		nltkstuff = NLTKanalysis()
		return render_template('analysis.html', data=nltkstuff.analysis(form.enteredtext.data))
	return render_template('index.html', form=form)

