from . import secret_key, mongo
from bson.objectid import ObjectId
import jwt


async def decode_token(token):
    return jwt.decode(token, secret_key, algorithms=["HS256"])["payload"]


async def login_required(token):
    collection = mongo["chat_levkovo"].users

    try:
        user_id = await decode_token(token)
    except:
        return

    current_user = await collection.find_one({"_id": ObjectId(user_id)})

    return current_user
