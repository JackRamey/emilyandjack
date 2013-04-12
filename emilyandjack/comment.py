from flask.ext.sqlalchemy import SQLAlchemy
from emilyandjack import app
from utilities import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    body = db.Column(db.String(4096))
    date = db.Column(db.DateTime)
    ip_addr = db.Column(db.String(24))

    def __init__(self, author, body, ip_addr):
        self.author = author
        self.body = body
        self.date = datetime.now()
        self.ip_addr = ip_addr

    def __repr__(self):
        return "<Comment: %r, %r>" % (self.id, self.date)

    def get_id(self):
        return self.id

def get_comment(cid):
    return Comment.query.filter_by(id=cid).first()

def init_comments():
    auth = 'Me of course!'
    body = 'You guys are awesome'
    c1 = Comment(auth, body)
    db.session.add(c1)
    db.session.commit()


