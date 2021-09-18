import random, asyncio, time

async def setup(num):
    while True:
        print(f"Log as {num} | {time.perf_counter()}")

async def play():
    runner = [
    await setup(_) for _ in range(1, 501)
    ]
    asyncio.wait()

asyncio.run(play())
