from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email_id = db.Column(db.String(300), nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)

    # 1st param: name of the target class
    # 2nd param: tablename of current class
    comments = db.relationship('Comment', backref='user')

class Destination(db.Model):
    __tablename__ = 'destination'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    currency = db.Column(db.String(3), nullable=False)
    image = db.Column(db.String(500), nullable=False)

    # 1st param: name of the target class
    # 2nd param: tablename of current class
    comments = db.relationship('Comment', backref='destination')

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now())

    # FK's
    user_id = db.Column(db.Integer,  db.ForeignKey('user.id'))
    destination_id = db.Column(db.Integer,  db.ForeignKey('destination.id'))
