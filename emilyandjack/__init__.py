from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from flask.ext.login import *

#create the app#
app = Flask(__name__)
app.config.from_pyfile('emilyandjack.cfg', silent=True)
login_manager = LoginManager()
login_manager.setup_app(app)

import emilyandjack.views
