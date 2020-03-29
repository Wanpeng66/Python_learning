# Python 3.5开始引入了新的语法async和await
# 来替代@asyncio.coroutine和yield from
import asyncio


async def hello():
    print("hello world")
    await asyncio.sleep(2)
    print("hello again...")

async def hello2():
    print("hello world2")
    await asyncio.sleep(1)
    print("hello2 again...")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([hello(),hello2()]))
    loop.close()