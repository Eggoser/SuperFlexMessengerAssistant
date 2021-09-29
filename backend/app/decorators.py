from flask import jsonify, request
from bson.objectid import ObjectId
from .auth import decode_token
from . import mongo
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace("Bearer ", "", 1)

        else:
            return jsonify({'message': 'a valid token is missing'})

        try:
            user_id = decode_token(token)

            current_user = mongo["chat_levkovo"].users.find({"_id": ObjectId(user_id)})[0]
            del current_user["_id"]
            print(current_user)
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator
