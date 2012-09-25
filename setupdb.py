from emilyandjack import app
from emilyandjack.utilities import db
from emilyandjack.user import User, init_users
from emilyandjack.post import Post, init_posts

db.create_all()
init_users()
init_posts()

