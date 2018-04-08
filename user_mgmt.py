from application.app import app, db
from application.models import User


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', action='store_true', help='Create all tables')
    parser.add_argument('-d', '--drop_all', action='store_true', help='Drop all tables')
    args = parser.parse_args()

    with app.app_context():
        if args.drop_all:
            db.drop_all()
        if args.create:
            db.create_all()
        
        # add dummy users
        User.create_user('user1', 'user1@place.org')
        User.create_user('user2', 'user2@place.org')

