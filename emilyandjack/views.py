from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from emilyandjack import app
from user import User, init_users
from post import Post
from database import db
from flask.ext.login import *

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['post'] != '':
            post = Post(request.form['post'], current_user)
            db.session.add(post)
            db.session.commit()
    #Populate the posts
    posts = Post.query.order_by(Post.date.desc())
    return render_template('welcome_page.html', posts=posts, user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    username = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user != None:
            #Check password
            if user.password == request.form['password']:
                login_user(user);
                flash('Log in status: EPIC SUCCESS!')
                return redirect(url_for('index'));
            else:
                error = 'Bad login.'
        else:
            error = 'User does not match any in our system!'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out.')
    return render_template('login.html')

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

#DEBUG
@app.route('/debug', methods=['GET', 'POST'])
def debugDB():
    if request.method == 'POST':
        #if button id is db
        flash(User.query.all())
        flash(Post.query.all())
        #else if button id is current_user
        flash(current_user)
    return render_template('debug.html')
