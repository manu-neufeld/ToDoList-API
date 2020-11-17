from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    task_relationship = db.relationship('Task', cascade="all, delete", lazy=True)

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "username": self.user_name,
            "task":self.task_relationship
            # do not serialize the password, its a security breach
        }
    
    def get_all_users(self):
        users = User.query.all()
        return users

    @classmethod
    def get_user(cls,  userRandom):
        user  = User.query.filter_by(user_name= userRandom)
        print(user)
        # all_users = list(map(lambda x: x.serialize(), user))
        # print(all_users)
        return user.serialize()
    
    def create_user(self):
        db.session.add(self)
        db.session.commit()
        return self.seriealize()
    
    def delete_user(user):
        person=User.query.filter_by(user_name=user).first()
        person.delete()
        db.session.commit()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(255), unique=False, nullable=False)
    done = db.Column(db.Boolean(False), unique=False, nullable=False)
    user_to_do = db.Column(db.String(80), db.ForeignKey("user.user_name"))
    

    # def __repr__(self):
    #     return f"task: {self.label}, done:{self.done}"
    
    def add_task(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def read_all_tasks(cls, user):
        tasks=Task.query.filter_by(user_to_do=user)
        all_tasks = list(map(lambda x: x.serialize(), tasks))
        return all_tasks

    def update_tasks(id, label, done):
        update=Task.query.get(id)
        update.label=label
        update.done=done
        db.session.commit()
    
    def serialize(self):
        return {
            "id": self.id,
            "user_to_do":self.user_to_do,
            "label": self.label,
            "done":self.done
            # do not serialize the password, its a security breach
        }
    # def __repr__(self):
    #     return '<User %r>' % self.username

    