import json, os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import *
from flask.ext.markdown import Markdown
from emilyandjack import app
from profile import Profile, load_from_json

#Set up SQLAlchemy
db = SQLAlchemy(app)

#Set up Login Manager
login_manager = LoginManager()
login_manager.setup_app(app)

#Set up Markdown
Markdown(app)

#Set up profiles
profiles = {}
with app.open_resource('static/json/profiles.json') as json_data:
    data = json.load(json_data)
    profiles = load_from_json(data)


#Full names dictionary
fullnames = {
    'bea': 'Bea Ramey',
    'dan': 'Dan Webster',
    'emily': 'Emily Webster',
    'jack': 'Jack Ramey',
    'jenna': 'Jenna Robles',
    'justin': 'Justin Cocke',
    'natasha': 'Natasha Vocelka',
    'nathan': 'Nathan Borgo'
}


