import uuid , datetime ,random
from . import db, UPLOAD_FOLDER

def generate_id():
    return int(str(uuid.uuid4().int)[:8])

def get_date():
    return datetime.datetime.now().today()

def generate_file_URI():
    return '/'+UPLOAD_FOLDER+str(uuid.uuid4().get_hex()[0:12])+'/'


class User(db.Model):
    __tablename__   = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True,nullable=False)
    location = db.Column(db.String(80))
    bio = db.Column(db.String(300))
    date_joined = db.Column(db.Date,nullable=False)
    file_URI = db.Column(db.String(80),nullable=False)

    def __init__(self,fname, lname, email, location, bio, id=None):
        if id: 
            self.id         = id
        else:
            self.id         = generate_id()
        self.email          = email
        self.fname          = fname 
        self.lname          = lname
        self.location       = location
        self.bio            = bio 
        self.date_joined    = get_date()
        self.file_URI       = generate_file_URI()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
