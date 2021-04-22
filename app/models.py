from . import db

class User(db.Model):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))
	name = db.Column(db.String(80))
	email = db.Column(db.String(80))
	location = db.Column(db.String(80))
	biography = db.Column(db.String(80))
	photo = db.Column(db.String(80))
	date_joined = db.Column(db.DateTime)	
	
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
	
    def __init__(self,username,password,name,email,location,biography,photo,date_joined):
		self.username = username
		self.password = password
		self.name = name
		self.email = email
		self.location = location
		self.biography = biography
		self.photo = photo
		self.date_joined = date_joined
		
		
class Car(db.Model):
	__tablename__ = 'Cars'
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String(80))
	make = db.Column(db.String(80))
	model = db.Column(db.String(80))
	colour = db.Column(db.String(80))
	year = db.Column(db.String(80))
	transmission = db.Column(db.String(80))
	car_type = db.Column(db.String(80))
	price = db.Column(db.decimal(10))
	user_id = db.Column(db.Integer, foreign_key=True)
	
	
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
	
    def __init__(self,description,make,model,colour,year,transmission,car_type,price,user_id):
		self.description = description
		self.make = make
		self.model = model
		self.colour = colour
		self.year = year
		self.transmission = transmission
		self.car_type = car_type
		self.price = price
		self.user_id = user_id
		
class Favourite(db.Model):
	__tablename__ = 'Favourites'
	id = db.Column(db.Integer, primary_key=True)
	car_id = db.Column(db.Integer, foreign_key=True)
	user_id = db.Column(db.Integer, foreign_key=True)
	
	
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
	
    def __init__(self,car_id,user_id):
		self.car_id = id
		self.user_id = user_id
	