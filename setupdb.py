from emilyandjack import app
from emilyandjack.utilities import db
from emilyandjack.user import User, init_users
from emilyandjack.post import Post, init_posts
from emilyandjack.comment import Comment, init_comments
from emilyandjack.link import Link, init_links

db.drop_all()
db.create_all()
init_users()
#init_posts()
#init_comments()
init_links()

