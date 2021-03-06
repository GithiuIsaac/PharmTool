from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from pharmtool import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    usertype = db.Column(db.String(20), nullable=False, default='Patient')
    records = db.relationship('Record', backref='author', lazy=True)
    # Backref allows the author attribute to get the User who created the record

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    # Set the secret key and expiration time, return the created token 
    # that alspo contains a payload of the user id

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    # Takes the token as the argument, creates the serializer and tries to load the token
    # If exception, return None. If no exception, it returns the user with that user id

    def __repr__(self):
        return f"User('{self.id}','{self.username}', '{self.email}', '{self.image_file}', '{self.usertype}')"


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fbs = db.Column(db.Float, nullable=False)
    rbs = db.Column(db.Float, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Record('{self.title}', '{self.date_posted}')"
