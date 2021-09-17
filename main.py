import random, asyncio

async def setup(count):
    result = random.randint(5, 16) * 0.01
    await asyncio.sleep(result)
    print("Log as {}".format(count))

async def play():
    await asyncio.wait([setup(_) for _ in range(1, 101)])
asyncio.run(play())
