# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持
# asyncio的编程模型就是一个消息循环
# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，
# 然后在coroutine内部用yield from调用另一个coroutine实现异步操作
import asyncio


def generator_1():
    total = 0
    while True:
        x = yield total
        print('加', x)
        if not x:
            break
        total += x
    return total


def generator_2():  # 委托生成器
    while True:
        total = yield from generator_1()  # 子生成器
        print('加和总数是:', total)


def main1():
    g2 = generator_2()
    total = g2.send(None)
    print(total)
    total = g2.send(2)
    print(total)
    total = g2.send(3)
    print(total)
    total = g2.send(None)
    print(total)


# 被@asyncio.coroutine修饰的方法就是异步方法
# 碰到yield from 语句，主线程就会暂时跳过这个任务，去执行其他任务
# 直到yield from后面的语句执行完，那么主线程就会从之前暂停的地方继续执行
@asyncio.coroutine  # 标志协程的装饰器
def hello():
    print("hello world")
    yield from asyncio.sleep(1)
    print("hello again...")


@asyncio.coroutine
def hello2():
    print("hello world2")
    yield from asyncio.sleep(1)
    print("hello 2 again...")


@asyncio.coroutine
def hello3():
    print("hello world3")
    yield from asyncio.sleep(1)
    print("hello 3 again...")


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_1():
    print('开始运行IO任务1...')
    yield from asyncio.sleep(1)  # 假设该任务耗时2s
    print('IO任务1已完成，耗时2s')
    return taskIO_1.__name__


@asyncio.coroutine  # 标志协程的装饰器
def taskIO_2():
    print('开始运行IO任务2...')
    yield from asyncio.sleep(3)  # 假设该任务耗时3s
    print('IO任务2已完成，耗时3s')
    return taskIO_2.__name__

@asyncio.coroutine
def taskIO_3():
    print("开始运行IO任务3...")
    print('IO任务3已完成，耗时0s')
    return taskIO_3.__name__

@asyncio.coroutine  # 标志协程的装饰器
def main():  # 调用方
    tasks = [taskIO_1(),taskIO_3(), taskIO_2()]  # 把所有任务添加到task中
    done, pending = yield from asyncio.wait(tasks)  # 子生成器
    # done是已完成任务的元组，pending是进行中任务的元组，所以返回结果需要逐个调用result()
    for r in done:
        print('协程无序返回值：' + r.result())


if __name__ == "__main__":
    #  main1()
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello2(), hello3()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(main())
    loop.close()
