from flask import Blueprint, render_template
from application.models import User

home = Blueprint('home', __name__)

@home.route('/', methods=["GET"])
def homepage():
    return render_template('home.html')


@home.route('/users', methods=['GET'])
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@home.route('/users/<string:username>', methods=['GET'])
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)
