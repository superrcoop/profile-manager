import datetime
from flask_mail import Message
from app import mail

def get_time():
	return datetime.datetime.now().year

# Configured to work with mailtrap.io | example emails do not work but message is deliverd @mailtrap.io
def send_mail(subject,name,email, text_body):
	msg = Message(subject, sender=(name,email), recipients=["email@example.com"])
	msg.body = text_body
	mail.send(msg)