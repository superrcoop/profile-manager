from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'passphrase' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' 
# Add your mailtrap username here
app.config['MAIL_USERNAME'] = '' 
# Add your mailtrap password here
app.config['MAIL_PASSWORD'] = '' 
 
mail = Mail(app) 

from app import views