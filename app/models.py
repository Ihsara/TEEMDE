
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(12))
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Emotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    timestamp= db.Column(db.DateTime, index=True, default=datetime.utcnow)




