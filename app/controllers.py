import os
from flask import flash , request, url_for
try:
    from urllib.parse import urlparse, urljoin # python 3 support
except ImportError:
     from urlparse import urlparse, urljoin # python 2 support
from .forms import ALLOWED_EXTENSIONS

def get_profile_photo():
    rootdir = os.getcwd()
    ls = []
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            ls.append(os.path.join(subdir, file).split('/')[-1])
    return ls

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc