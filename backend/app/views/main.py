from flask import request, Blueprint
from flask import jsonify as jsonify_flask
from ..decorators import login_required
from .. import mongo
from ..auth import encode_token
from ..google import is_valid_google_token

import datetime

main = Blueprint("api", __name__)

TOKEN_LIVE_TIME_MINUTES = 60 * 24


def jsonify(data):
    return jsonify_flask(data)


@main.route("/api/v1/send_message", methods=["POST"])
@login_required
def send_message(current_user):
    collection = mongo["chat_levkovo"]

    # будет принимать googleId пользователя, сообщение пользователя
    googleId, message, pofig = request.json["googleId"], request.json["message"], request.json.get("pofig") or False

    second_user = list(collection.users.find({"googleId": googleId}, {"_id": 0}))

    if not second_user:
        return "second user not exist"

    second_user = second_user[0]

    members = [
        current_user,
        second_user
    ]
    members_id = [
        current_user["googleId"],
        second_user["googleId"]
    ]

    message_dict = {
        "googleId": current_user["googleId"],
        "content": message,
        "date": datetime.datetime.now()
    }

    current_chat = list(collection.chats.find({"members": {"$in": members}}))

    # Обработка сообщения -
    # Обработка сообщения -
    # Обработка сообщения -

    if not current_chat:
        collection.chats.insert({
            "messages": [message_dict],
            "members": members,
            "members_id": members_id
        })

    else:
        current_chat = current_chat[0]
        current_chat["messages"] += [message_dict]

        collection.chats.update({"_id": current_chat["_id"]}, {"$set": {"messages": current_chat["messages"]}})

    return jsonify("success")


@main.route("/api/v1/user")
@login_required
def get_user(current_user):
    return jsonify(current_user)


@main.route("/api/v1/chats")
@login_required
def get_chats(current_user):
    def get_members(members_local):
        return [i for i in members_local if i["googleId"] != current_user["googleId"]][0]

    data = [{"last_message": i["messages"][-1], "member": get_members(i["members"])} for i in
            mongo["chat_levkovo"].chats.find({"members": {"$elemMatch": {"googleId": current_user["googleId"]}}},
                                             {"_id": 0})]

    return jsonify(data)


@main.route("/api/v1/users")
@login_required
def get_users(current_user):
    def get_members(members_local):
        return [i for i in members_local if i["googleId"] != current_user["googleId"]][0]["googleId"]

    collection = mongo["chat_levkovo"]
    # serializer = Serializer("id", "name", "email", "googleId", "avatarUrl")
    already_chats = [get_members(i["members"]) for i in
                     collection.chats.find({"members": {"$elemMatch": {"googleId": current_user["googleId"]}}},
                                           {"_id": 0})]
    print(already_chats)
    new_chats = [new_chat for new_chat in collection.users.find({}, {"_id": 0})
                 if new_chat["googleId"] not in already_chats and new_chat["googleId"] != current_user["googleId"]]

    return jsonify(new_chats)


@main.route("/api/v1/messages", methods=["POST"])
@login_required
def get_messages(current_user):
    # при запросе сообщений поставить флаг прочитано
    googleId = request.json["googleId"]
    chat = list(mongo["chat_levkovo"].chats.find({"members_id": {"$in": [current_user["googleId"], googleId]}}))[0]

    return jsonify(chat["messages"])


@main.route("/api/v1/auth/login", methods=["POST"])
def auth_login():
    token = request.json["token"]

    valid_token_data = is_valid_google_token(token)

    if not valid_token_data:
        return jsonify({"message": "invalid google token"})
    encoded_token = encode_token(str(valid_token_data["_id"]))

    return jsonify({
        "expire": TOKEN_LIVE_TIME_MINUTES * 60,
        "token": encoded_token,
    })
