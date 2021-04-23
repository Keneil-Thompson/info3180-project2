"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required 
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app.forms import UserForm, CarForm, LoginForm
from app.models import User, Car, Favourite
from datetime import date
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
import os


###
# Routing for your application.
###

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """
    Because we use HTML5 history mode in vue-router we need to configure our
    web server to redirect all routes to index.html. Hence the additional route
    "/<path:path".

    Also we will render the initial webpage and then let VueJS take control.
    """
    return render_template('index.html')
	
'''@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Christopher Martin, David Scott, Keneil Thompson, Shaquan Robinson")
'''
@app.route('/api/register', methods=['POST','GET'])
def register():
	form = UserForm()
	if request.method == 'POST' and form.validate_on_submit():
		photo = form.photo.data
		file = secure_filename(photo.filename)
		photo.save(os.path.join(app.config['UPLOAD_FOLDER'],file))
		entry = User(
		username = form.username.data,
		password = form.password.data,
		name = form.name.data,
		email = form.email.data,
		location = form.location.data,
		biography = form.biography.data,
		photo = file,
		date_joined = date.today())
		db.session.add(entry)
		db.session.commit()
		flash('Registration successfull')
		return jsonify({"message":"File Upload Successful"})
	else:
		return jsonify({"errors": form_errors(form)})
		#return redirect(url_for('home'))
	#return render_template('register.html',form=form)

@app.route('/api/auth/login', methods=['POST','GET'])
def login():
	form = LoginForm()
	if request.method == 'POST' and form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		user = User.query.filter_by(username=username).first()
		if user is not None and check_password_hash(user.password, password):
			login_user(user)
			flash("login successful")
			return redirect(url_for('home'))
		else :
			flash("invalid login")
	return render_template('login.html',form=form)

@login_required
@app.route('/api/auth/logout', methods=['POST','GET'])
def logout():
	logout_user()
	return render_template('home.html')
	
# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@login_required
@app.route('/api/cars', methods=['GET'])
def cars():
	"""Render website's home page."""
	cars = Car.query.all()
	return render_template('carlist.html',cars=cars)

@login_required
@app.route('/api/cars',  methods=['POST','GET'])
def addcars():
	"""Render website's home page."""
	form = CarForm()
	if request.method == 'POST' and form.validate_on_submit():
		photo = form.photo.data
		file = secure_filename(photo.filename)
		photo.save(os.path.join(app.config['UPLOAD_FOLDER'],file))
		entry = Car(
		description = form.description.data,
		make = form.make.data,
		model = form.model.data,
		colour = form.colour.data,
		year = form.year.data,
		transmission = form.transmission.data,
		car_type = form.car_type.data,
		price = form.price.data,
		photo = file,
		user_id = current_user.get_id())
		db.session.add(entry)
		db.session.commit()
		flash('Car successfully added')
		return redirect(url_for('home'))
	return render_template('addcar.html',form=form)

@app.route('/api/cars/{car_id}', methods=['GET'])
def carid():
    """Render website's home page."""
    return render_template('car.html')

@app.route('/api/cars/{car_id}/favourite', methods=['POST'])
def favourite():
    """Render website's home page."""
    return render_template('carlist.html')

@app.route('/api/cars/search', methods=['GET'])
def search():
    """Render website's home page."""
    return render_template('search.html')

@app.route('/api/users/{user_id}', methods=['GET'])
def userid():
    """Render website's home page."""
    return render_template('user.html')

@app.route('/api/users/{user_id}/favourites', methods=['GET'])
def userfav():
    """Render website's home page."""
    return render_template('favourites.html')

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages
	
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
