import asyncio


async def gatherfun(id, delay):
    print(f"Task {id} started")
    await asyncio.sleep(delay)
    print(f"Task {id} completed after {delay} seconds")
    return f"Result from task {id}"


async def main():
    results = await asyncio.gather(gatherfun(1, 2), gatherfun(2, 3), gatherfun(3, 4))
    for result in results:
        print(f"results is {result}")


asyncio.run(main())
