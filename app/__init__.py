from flask import Flask,Request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os , psycopg2

app = Flask(__name__)
app.config.from_object(__name__)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER='./app/static/uploads'
app.config['SECRET_KEY'] = 'Sup3r$3cret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

DATABASE_URL = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] 	= True
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db = SQLAlchemy(app)

from app import views