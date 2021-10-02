from app.clients import clients_server
import ssl

import asyncio

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain("./ucabix_com.crt", keyfile="./ucabix_com.key")


loop = asyncio.get_event_loop()

loop.run_until_complete(clients_server(ssl_context))
loop.run_forever()
