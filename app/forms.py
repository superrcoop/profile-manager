from wtforms import StringField, PasswordField  , HiddenField , SelectField
from wtforms.validators import Required,Length, Email,EqualTo ,DataRequired
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileAllowed, FileRequired


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

class AddProfile(FlaskForm):
    fname = StringField('First Name', validators=[Length(min=4, max=25,message=('Name does not satisfy condition ( 4 < name.length <= 25 )')),Required('Please provide a name')])
    lname = StringField('Last Name', validators=[Length(min=4, max=25,message=('Name does not satisfy condition ( 4 < name.length <= 25 )')),Required('Please provide a name')])
    gender = SelectField('Programming Language',choices=[('Male'), ('Female'), ('Decline to answer')],validators=[Required('Select a gender')])
    email = StringField('Email Address', validators=[Email(message='This is not a valid email'), Length(min=6, max=40,message=('Email does not satisfy condition ( 6 < email.length <= 40 )')),Required('Please provide an email address')])
    location = StringField('Location', validators=[Length(min=1, max=50)])
    bio = StringField('Biography', validators=[Length(min=3, max=500),Required('Say something about you')])
    photo= FileField('Upload', validators=[
        FileRequired(),
        FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')
    ])