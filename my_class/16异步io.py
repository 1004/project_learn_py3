"""
异步IO

模块： asyncio
异步框架： sanic


"""

import asyncio
import threading


@asyncio.coroutine
def hello():
    print("hhh")
    yield from asyncio.sleep(1)
    print("000")


if __name__ == '__main__':
    looper = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    looper.run_until_complete(asyncio.wait(tasks))
    looper.close()