from wtforms import Form, StringField, PasswordField  , HiddenField
from wtforms.validators import Required,Length, Email

class ContactForm(Form):
    name = StringField('Name', validators=[Length(min=4, max=25,message=('Name does not satisfy condition ( 4 < name.length <= 25 )')),Required('Please provide a name')])
    email = StringField('Email Address', validators=[Email(message='This is not a valid email'), Length(min=6, max=40,message=('Email does not satisfy condition ( 6 < email.length <= 40 )')),Required('Please provide an email address')])
    subject = StringField('Subject', validators=[Length(min=1, max=50)])
    message = StringField('Message', validators=[Length(min=3, max=500),Required('Enter a message')])
