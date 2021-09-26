from . import db


"""
With User and Chat MANY TO MANY relationship
With Chat and Message ONE TO MANY relationship
"""


class User(db.Model):
    chats = None


# create relationship with User
class Chat(db.Model):
    users = None
    messages = None


# create relationship with Chat
class Message(db.Model):
    chat = None
