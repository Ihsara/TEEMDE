
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




class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    angriness_level = db.Column(db.Float(precision=8))
    happiness_level = db.Column(db.Float(precision=8))

    def __repr__(self):
        return 'At {time}, angriness level was {angry}, happy level was {happy}.'.format(time=self.timestamp,
                                                                                            angry=self.angriness_level,
                                                                                            happy= self.happiness_level)

    def info(self):
        data = {}
        data['happiness'] = self.happiness_level
        data['angriness'] = self.angriness_level
        return data

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    timestamp= db.Column(db.DateTime, index=True, default=datetime.utcnow)
    text = db.Column(db.Text)
    polarity = db.Column(db.Float( precision = 8))
    subjectivity = db.Column(db.Float(precision =8))

    def info(self):
        data = {}
        sentiment = {}
        data["text"] = self.text
        sentiment["polarity"] = self.polarity
        sentiment["subjectivity"] = self.subjectivity
        data['sentiment'] = sentiment
        return data




