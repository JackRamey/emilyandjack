import json, os
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import *
from emilyandjack import app
from profile import Profile, load_from_json

#static dir location
STATIC_DIR = 'emilyandjack/static/'

#Set up SQLAlchemy
db = SQLAlchemy(app)

#Set up Login Manager
login_manager = LoginManager()
login_manager.setup_app(app)

#Set up profiles
profiles = load_from_json(os.path.join(STATIC_DIR, 'json/profiles.json'))

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


