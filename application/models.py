from datetime import datetime
from .ext import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    added_ts = db.Column(db.DateTime)
    last_login_ts = db.Column(db.DateTime)

    @classmethod
    def create_user(cls, username, email):
        """ Create a new user """
        new_user = User(username=username, email=email, added_ts=datetime.now())
        db.session.add(new_user)
        db.session.commit()

    def get_id(self, username):
        return self.query.filter_by(username=username).first()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


