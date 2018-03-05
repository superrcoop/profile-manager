"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db, login_manager
from .controllers import get_time ,get_uploaded_images , flash_errors , is_safe_url
from flask_login import login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from .forms import AddProfile
from werkzeug.datastructures import CombinedMultiDict



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/success')
def success():
    """Render website's success page."""
    return render_template('success.html')


@app.route('/add_profile',methods=['GET', 'POST'])
def add_profile():
    form = AddProfile(CombinedMultiDict((request.files, request.form)))
    if request.method == 'POST' and form.validate():
        f = form.photo.data
        filename = secure_filename(f.filename)
        # Get file data and save to your uploads folder
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Thanks for registering..')
        return redirect(url_for('success')) 
    return render_template('add_profile.html',form=form)

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
