import asyncio


async def main():
    print("this is coroutine")
    await asyncio.sleep(4)
    print("this is end")


def hello():
    print("hello")


asyncio.run(main())
