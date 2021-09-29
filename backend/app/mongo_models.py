from . import mongo
import datetime


def use_mongo():
    return mongo["chat_levkovo"]


class User:
    googleId = str()
    name = str()
    email = str()
    avatarUrl = str()
    chat_ids = []

    def __init__(self):
        self._collection = mongo["chat_levkovo"]["user"]

    def save(self):
        pass


class Chat:
    messages = []
    createdAt = datetime.datetime.now()

    def __init__(self):
        self._collection = mongo["chat_levkovo"]["user"]

    def save(self):
        pass


class Message:
    content = str()
    chat_id = int()

    createdAt = datetime.datetime.now()

    def __init__(self, **kwargs):
        self._collection = mongo["chat_levkovo"]["user"]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        pass
