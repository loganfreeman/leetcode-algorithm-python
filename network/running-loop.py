import asyncio
import socket


async def wait_for_data():
    loop = asyncio.get_running_loop()

    rsock, wsock = socket.socketpair()

    reader, writer = await asyncio.open_connection(sock=rsock)

    loop.call_soon(wsock.send, 'abc'.encode())

    data = await reader.read(100)

    print("Received:", data.decode())

    writer.close()

    wsock.close()

asyncio.run(wait_for_data())
