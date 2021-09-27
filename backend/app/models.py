
import datetime
from . import db

"""
With User and Chat MANY TO MANY relationship
With Chat and Message ONE TO MANY relationship
"""

user_chat_association = db.Table('association', db.Model.metadata,
                                 db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                 db.Column('chat_id', db.Integer, db.ForeignKey('chats.id'))
                                 )


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)

    googleId = db.Column(db.String(50), unique=True, index=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    avatarUrl = db.Column(db.String(120))
    chats = db.relationship("Chat", secondary=user_chat_association)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    createdAt = db.Column(db.DateTime, default=datetime.datetime.now())


# create relationship with User
class Chat(db.Model):
    __tablename__ = "chats"
    id = db.Column(db.Integer, primary_key=True)
    # users = None
    messages = db.relationship("Message", backref="chat", lazy='dynamic')
    createdAt = db.Column(db.DateTime, default=datetime.datetime.now())


# create relationship with Chat
class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.Text)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    # chat = db.relationship('Chat')

    createdAt = db.Column(db.DateTime, default=datetime.datetime.now())


