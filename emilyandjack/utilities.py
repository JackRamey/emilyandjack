from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import *
from emilyandjack import app

#Set up SQLAlchemy
db = SQLAlchemy(app)

#Set up Login Manager
login_manager = LoginManager()
login_manager.setup_app(app)

