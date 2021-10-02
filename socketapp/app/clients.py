import asyncio
import json
import websockets

from . import update_dictionary, debug
from .mongo_helpers import get_messages, send_message, get_chats, get_users, jsonify
from .decorators import login_required


async def channel_get_messages(current_user, ws, params, as_id=None):
    user_id = current_user["googleId"]

    print("GEt messages:", current_user["name"], params["googleId"])

    try:
        encoded_messages = await get_messages(user_id, params["googleId"])
        await ws.send(encoded_messages)

    except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError):
        del update_dictionary[user_id].callbacks[as_id]


async def channel_send_message(current_user, ws, params):
    try:
        user_id = current_user["googleId"]
        user_second_id = params["googleId"]

        returned_data, executed = await send_message(current_user, params["googleId"], params["message"], params["ignore"])

        # if returned_data == "success":
        await ws.send(returned_data)

        if executed:
            update_dictionary[user_id].value = True
            update_dictionary[user_second_id].value = True
    except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError):
        pass


async def channel_get_users(current_user, ws, params, as_id=None):
    try:
        data = await get_users(current_user)
        await ws.send(data)
    except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError):
        del update_dictionary[current_user["googleId"]].callbacks[as_id]


async def channel_get_chats(current_user, ws, params, as_id=None):
    try:
        data = await get_chats(current_user)
        await ws.send(data)
    except (websockets.exceptions.ConnectionClosedOK, websockets.exceptions.ConnectionClosedError):
        del update_dictionary[current_user["googleId"]].callbacks[as_id]

flags = {
    "messages": channel_get_messages,
    "send_message": channel_send_message,
    "users": channel_get_users,
    "chats": channel_get_chats
}


async def main_echo(websocket, path):
    async for message in websocket:
        data = json.loads(message)

        # проверяем авторизацию
        current_user = await login_required(data.get("Authorization"))

        task_types = data["types"]
        params = data.get("params") or {}

        # не прошел авторизацию
        if not current_user:
            print("no auth")
            return "auth required"

        for task_type_local in task_types:
            # это функция
            current_task = flags[task_type_local]
            # выполняется единожды
            if task_type_local == "send_message":
                # задача на отправку сообщения ассинхронная, callback там же
                asyncio.get_event_loop().create_task(channel_send_message(current_user=current_user, ws=websocket, params=params))

            # создаем канал с прослушиванием
            else:
                asyncio.get_event_loop().create_task(current_task(current_user=current_user, ws=websocket, params=params))
                update_dictionary[current_user["googleId"]].new_callback(current_task,
                                                                         current_user=current_user,
                                                                         ws=websocket,
                                                                         params=params)

        print("connected:", current_user["googleId"])


def clients_server(ssl_local):
    print("start clients..")
    if debug:
        server = websockets.serve(main_echo, "0.0.0.0", 5050, reuse_port=True)
    else:
        server = websockets.serve(main_echo, "0.0.0.0", 5050, reuse_port=True, ssl=ssl_local)
    return server
