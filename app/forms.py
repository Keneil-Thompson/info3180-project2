from flask_wtf import FlaskForm
from wtforms import SelectField, TextField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class UserForm(FlaskForm):	
	description = TextAreaField('Description',[DataRequired()])
	make = TextField('Make',[DataRequired()])
	model = TextField('Model',[DataRequired()])
	colour = TextField('Colour',[DataRequired()])
	year = TextField('Year', [DataRequired()])
	transmission = TextField('Transmission', [DataRequired()])
	car_type = TextField('Car Type', [DataRequired()])
	price = TextField('Price',[DataRequired()])
	photo = FileField('Photo',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])
	
class CarForm(FlaskForm):
	pass
	
class FavouriteForm(FlaskForm):
	pass