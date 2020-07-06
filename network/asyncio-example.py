import asyncio
import time


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
asyncio.run(main())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main2())
