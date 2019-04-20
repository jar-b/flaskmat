from flask import Flask
from application import config
from .views.home import home
from .models import User
from .ext import db, login_manager

app = Flask(__name__)
app.config.from_object(config)

# register blueprints
app.register_blueprint(home)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/application.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# login manager
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    return User.get(username)
