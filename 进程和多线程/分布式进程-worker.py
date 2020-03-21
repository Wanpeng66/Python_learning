import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == "__main__":
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register("get_task")
    QueueManager.register("get_result")


    server_addr = "localhost"
    print("connect to %s " %server_addr)
    # 绑定ip 端口和秘钥
    manager = QueueManager(address=(server_addr,9090),authkey=b"abc")
    # 连接master
    manager.connect()

    # 从master获得两个队列
    task = manager.get_task()
    result = manager.get_result()
    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')