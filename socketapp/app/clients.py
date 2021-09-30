import asyncio
import json
import websockets
from . import update_dictionary


async def echo_websocket_test(user_id, ws):
    while True:
        try:
            if update_dictionary.get(user_id):
                print("event: ", user_id)
                await ws.send("update")
                update_dictionary[user_id] = False
        except websockets.exceptions.ConnectionClosedOK:
            print("error connect")
            return
        await asyncio.sleep(0.1)


async def echo_clients(websocket, path):
    while True:
        try:
            data = json.loads(await websocket.recv())
        except websockets.exceptions.ConnectionClosedOK:
            continue

        user_id = data["googleId"]
        asyncio.get_event_loop().create_task(echo_websocket_test(user_id, websocket))

        print("connected:", user_id)
        await websocket.send("hello world")


def clients_server(ssl_local):
    print("start clients..")
    server = websockets.serve(echo_clients, "0.0.0.0", 5050, reuse_port=True, ssl=ssl_local)
    return server
