from app.application import application_server
from app.clients import clients_server

import asyncio
# import websockets
# from websockets.server import WebSocketServerProtocol

loop = asyncio.get_event_loop()

loop.run_until_complete(clients_server())
loop.run_until_complete(application_server())
loop.run_forever()


# asyncio.get_event_loop().run_forever()
