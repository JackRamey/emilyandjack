from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

#create the app#
app = Flask(__name__)
app.config.from_pyfile('emilyandjack.cfg', silent=True)

import emilyandjack.views
