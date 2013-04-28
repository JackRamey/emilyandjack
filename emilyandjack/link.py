from flask.ext.sqlalchemy import SQLAlchemy
from emilyandjack import app
from utilities import db
from datetime import datetime
from flask import url_for

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    tag_id = db.Column(db.String(24))
    link = db.Column(db.String(1024))

    def __init__(self, tag_id, link):
        self.tag_id = tag_id
        self.link = link

    def __repr__(self):
        return "<Link: %r, %r>" % (self.id, self.link)

    def get_button_html(self, linkText):
        return "<form action=%s method=post><button class=\"btn btn-link\" type=submit id=%s method=post>%s</button></form>" % (url_for('link_click', link_id=self.tag_id), self.tag_id, linkText)

def get_link(linkid):
    return Link.query.filter_by(tag_id=linkid).first()

class LinkClick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    ip_addr = db.Column(db.String(24))
    #Foreign Key
    link_id = db.Column(db.Integer, db.ForeignKey('link.id'))
    link = db.relationship('Link',
        backref=db.backref('linkclicks', lazy='dynamic'))

    def __init__(self, ip_addr, link):
        self.date = datetime.now()
        self.ip_addr = ip_addr
        self.link = link

    def __repr__(self):
        return "<LinkClick: %r, %r, %r>" % (self.link, self.ip_addr, self.date)

def init_links():
    l = Link('engagement_zip', 'https://dl.dropboxusercontent.com/s/lvuxel5hkhuhuj2/Emily_and_Jack_Engagement_San_Francisco-01.zip?token_hash=AAGrEiNOufvipPu1We5Q88tF6EjvXzlCR5n1f2DY70fOSQ&dl=1')
    db.session.add(l)
    db.session.commit()
