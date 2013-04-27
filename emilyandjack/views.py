from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from emilyandjack import app
from user import User
from post import Post, get_post
from comment import Comment
from link import Link, LinkClick, get_link
from utilities import db, fullnames, profiles
from flask.ext.login import *
from datetime import date

@app.route('/', methods=['GET', 'POST'])
@app.route('/News', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        if request.form['post'] != '':
            html_enabled = False
            if 'html_enabled' in request.form:
                html_enabled = True
            post = Post(request.form['post'], current_user, html_enabled)
            db.session.add(post)
            db.session.commit()
    #Populate the posts
    posts = Post.query.order_by(Post.date.desc())
    days = days_remaining() 
    percent = percent_remaining()
    barstyle = bar_style()
    return render_template('welcome_page.html', posts=posts,
        user=current_user, days=days, percent=percent,
        barstyle=barstyle, get_link=get_link)

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
                return redirect(url_for('news'));
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

@app.route('/Post/Delete/<int:post_id>', methods=['GET', 'POST'])
def post_delete(post_id):
    if(current_user.is_admin()):
        db.session.delete(get_post(post_id))
        db.session.commit()
    return redirect(url_for('news'))

@app.route('/YourStories', methods=['GET', 'POST'])
def wallboard():
    if request.method == 'POST':
        if request.form['author'] != "" \
                and request.form['body'] != "" \
                and request.form['bot_stop'] == '7':
            comment = Comment(request.form['author'], request.form['body'], request.remote_addr)
            db.session.add(comment)
            db.session.commit()
        elif request.form['bot_stop'] != '7':
            flash('You did not answer the question properly. Sorry.')
    comments = Comment.query.order_by(Comment.date.desc())
    return render_template('wallboard_page.html', comments=comments)

@app.route('/WeddingParty')
def weddingparty():
    return render_template('weddingparty_page.html', name="")

@app.route('/WeddingParty/<name>')
def weddingparty_info(name=None):
    profile = profiles[name.lower()]
    return render_template('weddingparty_page.html', name=name, \
        profile=profile)

@app.route('/WeddingDetails')
def details():
    return render_template('details_page.html')

@app.route('/Registries')
def registries():
    return render_template('registries_page.html')

@app.route('/success')
def success():
    return render_template('success.html')

def days_remaining():
    enddate = date(2013, 7, 20)
    return (enddate - date.today()).days

def percent_remaining():
    startdate = date(2012, 7, 27)
    enddate = date(2013, 7, 20)
    denom = float((enddate - startdate).days)
    remain = float((enddate - date.today()).days)
    percent_remaining = int(100 - (remain / denom) * 100)
    if percent_remaining > 100:
        percent_remaining = 100
    return percent_remaining

def bar_style():
    pr = percent_remaining()
    if pr < 33:
        return "progress-success"
    elif pr < 66:
        return "progress-warning"
    else:
        return "progress-danger"

#LOGGING
@app.route('/link_click/<link_id>', methods=['POST'])
def link_click(link_id):
    l = get_link(link_id)
    lc = LinkClick(request.remote_addr, l)
    db.session.add(lc)
    db.session.commit()
    return redirect(l.link);

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
