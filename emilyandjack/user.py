from flask.ext.sqlalchemy import SQLAlchemy
from emilyandjack import app, login_manager
from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256))
    displayname = db.Column(db.String(80))
    active = db.Column(db.Boolean)

    def __init__(self, username, password, displayname, active=False):
        self.username = username
        self.password = password
        self.displayname = displayname
        self.active = active

    def __repr__(self):
        return '<User %r, %r, %r, %r>' % (self.username, \
            self.password, self.displayname, self.active)

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(username=userid).first()

def init_users():
    jack = User('jack', 'omgcat', 'Jack', active=True)
    emily = User('emily', 'omgcat', 'Emily', active=True)
    db.session.add(jack)
    db.session.add(emily)
    db.session.commit()


