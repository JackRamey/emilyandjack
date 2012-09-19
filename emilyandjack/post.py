from flask.ext.sqlalchemy import SQLAlchemy
from emilyandjack import app
from database import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1024))
    date = db.Column(db.DateTime)
    #Foreign Key
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', 
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, body, author):
        self.body = body
        self.author = author
        self.date = datetime.now()

    def __repr__(self):
        return "<Post: %r, %r>" % (self.title, self.author) 

    def get_id(self):
        return self.id

def init_posts():
    from user import User
    jack = User.query.filter_by(username='jack').first()
    post1 = Post('Test body', jack)
    db.session.add(post1)
    db.session.commit()

