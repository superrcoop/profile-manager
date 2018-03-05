from flask import Flask

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'Sup3r$3cret'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

from app import views