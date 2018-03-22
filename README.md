
Flask Profile Manager
-------------------------------------

> includes Flask-Login and Flask-SQLAlchemy

Description
-------------------

Template for login management in flask apps with incresed security


Getting Started !
-------------------

This Web app requires the latest version of [Python and Flask](http://flask.pocoo.org)

Clone the repository:

`$ git clone https://github.com/superrcoop/profile-manager.git`

Go into the repository:

`$ cd profile-manager`

Create a virtual environment and Install app dependencies:

`$ virtualenv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

Deploy
--------

Locally: 

~~~~python
app.config['SQLALCHEMY_DATABASE_URI'] =  '<database_url>'
~~~~

`$ python run.py`


Heroku:

Now we'll face some problem regarding migrating. What we'll do is below in order to bypass the problems.

~~~~
heroku run python
>> import os
>> os.environ.get('DATABASE_URL')
~~~~

~~~~python
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ('DATABASE_URL')
~~~~

Setup database: 

~~~
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
~~~

View database from heroku-cli:

~~~
heroku pg:psql

<heroku-app>::DATABASE=>\c
You are now connected to database "<heroku_database>" as user "<heroku_database_user>"

<heroku-app>::DATABASE=>\dt
                  List of relations
 Schema |      Name       |   Type   |     Owner      
--------+-----------------+----------+----------------
 public | alembic_version | table    | tamkdcawqlwozy
 public | profiles        | table    | tamkdcawqlwozy
(2 rows)

