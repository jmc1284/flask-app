from flask import Flask, render_template, url_for, request
from forms import BMIForm, RetirementForm
from bmi import *
from retirement import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f31f61393bc1158e5810413b02ccc13d'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
	form = BMIForm()
	if form.validate_on_submit():
		height_ft = int(request.form['height_ft'])
		height_in = int(request.form['height_in'])
		weight = int(request.form['weight'])
		bmi = calculate_bmi(height_ft, height_in, weight)
		category = get_category(bmi)
		return render_template('bmiresults.html', title='BMI Results', bmi=bmi, category=category)
	return render_template('bmi.html', title='BMI Calculator', form=form)

@app.route('/retirement', methods=['GET', 'POST'])
def retirement():
	form = RetirementForm()
	if form.validate_on_submit():
		age = int(request.form['age'])
		salary = int(request.form['salary'])
		percentage = int(request.form['percentage'])
		goal = int(request.form['goal'])
		retirement_age = calculate_retirement(age, salary, percentage, goal)
		return render_template('retirementresults.html', title='Retirement Age Results', retirement_age = retirement_age, goal = goal)
	return render_template('retirement.html', title='Retirement Age Calculator', form=form)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

