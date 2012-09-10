from flask.ext.sqlalchemy import SQLAlchemy
from emilyandjack import app, db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  password = db.Column(db.String(256))
  active = db.Column(db.Boolean)

  def __init__(self, username, password, active=False):
    self.username = username
    self.password = password
    self.active = active

  def __repr__(self):
    return '<User %r>' % self.username

def init_users():
  jack = User('jack', 'omgcat', active=True)
  emily = User('emily', 'omgcat', active=True)


