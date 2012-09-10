from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import *

#create the app#
app = Flask(__name__)
app.config.from_envvar('EJ_SETTINGS', silent=True)
db = SQLAlchemy(app)
login_manager = LoginManager()

@app.route('/')
def index():
    return render_template('welcome_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    flash(User.query.all())
  return render_template('login.html', error=error)

@app.route('/OurStory')
def story():
    return render_template('story_page.html')

@app.route('/OurEngagement')
def engagement():
    return render_template('engagement_page.html')

@app.route('/WeddingParty')
def weddingparty():
    return render_template('weddingparty_page.html')

@app.route('/WeddingDetails')
def details():
    return render_template('details_page.html')

@app.route('/Registries')
def registries():
    return render_template('registries_page.html')

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

