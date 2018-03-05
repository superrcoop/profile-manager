
Flask-Mail and Flask-WTF tutorial
-------------------------------------

> See Release version 1.0

Description
-------------------

info3180-lab3


Getting Started !
-------------------

This Web app requires the latest version of [Python and Flask](http://flask.pocoo.org)

Clone the repository:

`$ git clone https://github.com/superrcoop/info3180-lab3.git`

Go into the repository:

`$ cd info3180-lab3`

Create a virtual environment and Install app dependencies:

`$ virtualenv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

To allow Flask-Mail to work you'll need to configure your SMTP in `__init__.py`:

```python 
app.config['SECRET_KEY'] = 'passphrase' 
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io' 
app.config['MAIL_PORT'] = '465' 

# Add your mailtrap username here
app.config['MAIL_USERNAME'] = '' 

# Add your mailtrap password here
app.config['MAIL_PASSWORD'] = '' 
```

Run the app:

`$ python app.py`



