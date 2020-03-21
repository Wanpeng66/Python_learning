# 通过封装好的组件将某台计算机上的python对象通过网络暴露出去，在其他计算机上能使用
# 案例：一台机器发布任务，另一台机器处理任务，通过queue来进行解耦
import queue
import random
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

# 先声明两个队列
task = queue.Queue()
result = queue.Queue()

def getTask():
    return  task
def getResult():
    return result

if __name__ == "__main__":


    # 将两个队列注册到manager中
    # windows下不能用lamda,必须显示声明回调函数
    QueueManager.register("get_task",callable=getTask)
    QueueManager.register("get_result",callable=getResult)
    # 给manager设置ip 端口以及秘钥
    manager = QueueManager(address=("localhost",9090),authkey=b"abc")
    manager.start()

    taskQueue = manager.get_task()
    resultQueue = manager.get_result()

    # 将任务放进任务队列
    for i in range(10):
        n = random.randint(0, 10000)
        print("put %s put into taskQueue" %n)
        taskQueue.put(n)

    # 尝试从结果队列中拿到结果
    print("try to get result")
    for i in range(10):
        val = resultQueue.get(timeout=100)
        print("get %s from result" %val)

    manager.shutdown()
    print("master end ...")

