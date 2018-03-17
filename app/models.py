import uuid 
from . import db

def generate_id():
    return int(str(uuid.uuid4().int)[:8])

class UserProfile(db.Model):
    __tablename__   = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True,nullable=False)
    location = db.Column(db.String(80))
    bio = db.Column(db.String(300))
    file_URI = db.Column(db.String(125),nullable=False)

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
        self.file_URI       = str(self.id)


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
