from flask import Flask,Request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Sup3r$3cret'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://testuser:password@localhost/profilemanager"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)
# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config.from_object(__name__)
from app import views