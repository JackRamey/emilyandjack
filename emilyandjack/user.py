from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import AnonymousUser
from emilyandjack import app
from utilities import db, login_manager

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(256))
    displayname = db.Column(db.String(80))
    authenticated = db.Column(db.Boolean)
    active = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    def __init__(self, username, password, displayname, \
            authenticated=False, active=False, \
            anonymous=False, admin=False):
        self.username = username
        self.password = password
        self.displayname = displayname
        self.authenticated = authenticated
        self.active = active
        self.admin = admin

    def __repr__(self):
        return '<User %r, %r, %r>' % (self.username, \
            self.displayname, self.active)

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.admin

    def get_id(self):
        return self.username

class Anonymous(AnonymousUser):
    def is_admin(self):
        return False

@login_manager.user_loader
def load_user(userid):
    return User.query.filter_by(username=userid).first()

login_manager.anonymous_user = Anonymous

def init_users():
    jack = User('jack', 'omgcat', 'Jack', authenticated=True, \
        active=True, admin=True)
    emily = User('emily', 'omgcat', 'Emily', authenticated=True, \
        active=True, admin=True)
    db.session.add(jack)
    db.session.add(emily)
    db.session.commit()


