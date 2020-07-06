import asyncio


@asyncio.coroutine
def old_style_coroutine():
    print('sleep for one second')
    yield from asyncio.sleep(1)


async def main():
    await old_style_coroutine()

asyncio.run(main())
