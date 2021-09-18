import random, asyncio

num = int(input("Введите количество потоков: "))

async def setup(count):
    result = random.randint(5, 20) * 0.01
    await asyncio.sleep(result)
    print("Log as {}".format(count))

async def play(num):
    await asyncio.wait([setup(_) for _ in range(1, num+1)])

asyncio.run(play(num))
