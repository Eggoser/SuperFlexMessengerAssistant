import json
import datetime
from . import mongo, debug, max_neg_value
if not debug:
    from .neural import get_message_preprocessed_data_list


async def jsonify(data, channel_type):
    return json.dumps({"type": channel_type, "data": data}, ensure_ascii=False, default=str)


async def get_chats(current_user):
    async def get_members(members_local):
        return [i for i in members_local if i["googleId"] != current_user["googleId"]][0]

    data = [{"last_message": i["messages"][-1], "member": await get_members(i["members"]), "_id": i["_id"]}
            async for i in mongo["chat_levkovo"].chats.find({"members": {"$elemMatch": {"googleId": current_user["googleId"]}}})]

    return await jsonify(data, "chats")


async def get_users(current_user):
    async def get_members(members_local):
        return [i for i in members_local if i["googleId"] != current_user["googleId"]][0]["googleId"]

    collection = mongo["chat_levkovo"]
    already_chats = [await get_members(i["members"]) async for i in
                     collection.chats.find({"members": {"$elemMatch": {"googleId": current_user["googleId"]}}})]
    new_chats = [new_user async for new_user in collection.users.find({})
                 if new_user["googleId"] not in already_chats and new_user["googleId"] != current_user["googleId"]]

    return await jsonify(new_chats, "users")


async def get_messages(googleId, googleIdsecond):
    chat = [i async for i in mongo["chat_levkovo"].chats.find({"members_id": {"$all": [googleId, googleIdsecond]}})]
    if not chat:
        return await jsonify([], "messages")

    return await jsonify({"messages": chat[0]["messages"], "googleId": googleIdsecond}, "messages")


async def send_message(current_user, googleIdSecond, message, ignore=False):
    collection = mongo["chat_levkovo"]

    second_user = await collection.users.find_one({"googleId": googleIdSecond})

    if not second_user:
        return "second user not exist"

    members = [
        current_user,
        second_user
    ]
    members_id = [
        current_user["googleId"],
        second_user["googleId"]
    ]

    print(members[1]["name"], members[0]["name"])

    message_dict = {
        "googleId": current_user["googleId"],
        "content": message,
        "date": datetime.datetime.now()
    }

    current_chat = await collection.chats.find_one({"members_id": {"$all": members_id}})
    # current_chat = await collection.chats.delete_many({"members_id": {"$in": members_id}})

    # обработка ML
    predict_message = {}

    if not ignore:
        if debug:
            predict_message = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}
        else:
            predict_message = get_message_preprocessed_data_list(message)

        match = predict_message.get("neg") - predict_message.get("pos") / 2 - predict_message.get(
            "pos") / 4 - predict_message.get("neu") / 6

        with open("value.txt", "w") as log:
            log.write(str(match))

        if match > max_neg_value:
            return await jsonify({"googleId": googleIdSecond, "message": message, "type": "error"}, "message"), False

    # конец обработки ML
    if not current_chat:
        await collection.chats.insert_one({
            "messages": [message_dict],
            "members": members,
            "members_id": members_id,
            "predicts_for_message": predict_message
        })

        print("create chat")

    else:
        current_chat["messages"] += [message_dict]

        print("update chat")

        print(current_chat["_id"])

        await collection.chats.update_one({"_id": current_chat["_id"]}, {"$set": {"messages": current_chat["messages"]}})

    return await jsonify({"googleId": googleIdSecond, "message": message, "type": "success"}, "message"), True
