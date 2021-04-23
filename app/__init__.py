from flask import Flask
from .config import Config
from flask_sqlaclchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)
from app import views