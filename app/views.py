"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
"""
import os
from flask import send_from_directory
from app import app,db, login_manager
from .controllers import get_profile_photo , flash_errors , is_safe_url, allowed_file
from flask_login import login_user, logout_user, current_user
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
from .forms import AddProfile
from .models import User
from werkzeug.datastructures import CombinedMultiDict


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/success')
def success():
    """Render website's success page."""
    return render_template('success.html')


@app.route('/profile')
def profile():
    """Render website's profile"""
    return render_template('profile.html')


@app.route('/view_profile')
def view_profile():
    """Render website's view_profile"""
    return render_template('view_profile.html')


@app.route('/add_profile',methods=['GET', 'POST'])
def add_profile():
    error=None 
    form = AddProfile(CombinedMultiDict((request.files, request.form)))
    if request.method == 'POST' and form.validate_on_submit():
        fname, lname, email,location,bio = [form.fname.data, form.lname.data, form.email.data, form.location.data, form.bio.data]
        file = form.photo.data
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            error='No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not User.query.filter_by(email = email).first():
                user = User(fname = fname, lname = lname, email = email, location=location,bio=bio)
                file.save(os.path.join(user.file_URI, filename))
                db.session.add(user)
                db.session.commit()
            else:
                error='Email already exists'
        else:
            error='File now allowed'
        flash('Thanks for registering..')
        return redirect(url_for('success')) 
    return render_template('add_profile.html',form=form,error=error)

"""
The functions below should be applicable to all Flask apps.

"""
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
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
