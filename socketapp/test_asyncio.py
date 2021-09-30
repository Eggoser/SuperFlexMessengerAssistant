import asyncio


async def hello():
    while True:
        print("hello world")
        await asyncio.sleep(3)


async def hello_2():
    while True:
        print("hello world")
        await asyncio.sleep(3)


asyncio.get_event_loop().create_task(hello())
asyncio.get_event_loop().create_task(hello_2())
asyncio.get_event_loop().run_forever()
