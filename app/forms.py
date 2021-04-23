from flask_wtf import FlaskForm
from wtforms import SelectField, TextField, TextAreaField, PasswordField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email

class CarForm(FlaskForm):	
	description = TextAreaField('Description',[DataRequired()])
	make = TextField('Make',[DataRequired()])
	model = TextField('Model',[DataRequired()])
	colour = TextField('Colour',[DataRequired()])
	year = TextField('Year', [DataRequired()])
	transmission = TextField('Transmission', [DataRequired()])
	car_type = TextField('Car Type', [DataRequired()])
	price = TextField('Price',[DataRequired()])
	photo = FileField('Photo',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])
	
class UserForm(FlaskForm):
	username = TextField('Username',[DataRequired()])
	password = TextField('Password',[DataRequired()])
	name = TextField('Name',[DataRequired()])
	email = TextField('Email',[DataRequired(),Email()])
	location = TextField('Location', [DataRequired()])
	biography = TextField('Biography', [DataRequired()])
	photo = FileField('Photo',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])
	
class FavouriteForm(FlaskForm):
	pass

class LoginForm(FlaskForm):
	username = TextField('Username',[DataRequired()])
	password = PasswordField('Password',[DataRequired()])