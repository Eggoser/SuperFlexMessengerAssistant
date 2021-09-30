import asyncio
import json
import websockets
from . import update_dictionary, secret_key


async def echo_application(websocket, path):
    while True:
        try:
            data = json.loads(await websocket.recv())

            if secret_key != data["secret_key"]:
                await websocket.send("invalid auth")
                return

            user_id = data["googleId"]
            print("From application:", user_id)

            update_dictionary[user_id] = True
            await websocket.send("success")
        except websockets.exceptions.ConnectionClosedOK:
            continue


def application_server():
    print("start applications..")
    server = websockets.serve(echo_application, "localhost", 8769, reuse_port=True)
    return server
