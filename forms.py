from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class BMIForm(FlaskForm):
	height_ft = IntegerField('Height Feet', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1)])
	height_in = IntegerField('Height Inches', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=0, max=11)])
	weight = IntegerField('Weight', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1)])
	submit = SubmitField('Submit')

class RetirementForm(FlaskForm):
	age = IntegerField('Age', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1)])
	salary = IntegerField('Annual Salary', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1)])
	percentage = IntegerField('Percentage Saved Annualy', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1, max=100)])
	goal = IntegerField('Savings Goal', validators = [InputRequired(message='Please enter a valid integer'), NumberRange(min=1)])
	submit = SubmitField('Submit')