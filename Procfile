init: python flask-migrate.py db init
migrate: python flask-migrate.py db migrate
upgrade: python flask-migrate.py db upgrade
web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
