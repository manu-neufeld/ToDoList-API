from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeingKey, Integer, String


db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_to_do = db.Column(db.String(80),db.ForeingKey("User.user_name"))
    label = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(False), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }