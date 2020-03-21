# multiprocessing模块就是跨平台版本的多进程模块
# 感觉python中进程与java中线程使用类似
import os
import random
import subprocess
import time
from multiprocessing import Process, Lock, Pool,Queue

def basic_run(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
# 下面是进程的基本使用，新建，运行
def basic_process():
    print("parent is processing %s " % os.getpid())
    # target代表进程要运行的方法，name为进程的名字，args为运行方法的参数
    p = Process(target=basic_run, name="子进程", args=("子进程",))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
def concurrency_run(name,lock):
    # lock.acquire()
    print("子进程 %s 获得锁执行代码..." % name)
    # lock.release()
# 进程之间如果共享临界变量或临界区域 也需要加锁
def concurrency_process():
    print("parent is processing %s " % os.getpid())
    print("parent will creat 10 processes to run method concurrency_run with lock")
    # Lock为不可重入锁，RLock为可重入锁，Semaphore为python的信号量，Condition为python的条件变量
    lock = Lock()
    for i in range(10):
        p = Process(name="进程"+str(i),target=concurrency_run,args=(i,lock))
        p.start()
    print("end...")

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
def process_pool(i):
    pool = Pool(i)
    for k in range(int(i)):
        pool.apply_async(func=basic_run,args=(str(k)))
    pool.close()
    pool.join()
    print("进程全部执行完...")


# subprocess模块允许你启动一个新的进程，连接输入/输出/错误的管道， 获得子进程的返回码
# 相当于新建一个子进程帮忙做事，阻塞等待子进程结果
def test_subprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)


def provider(queue):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        queue.put(value)

def consumer(queue):
    print('Process to read: %s' % os.getpid())
    while True:
        value = queue.get(True)
        print('Get %s from queue.' % value)

# 进程间通信，可以使用queue来进行 生产者-消费者
def communicateWithQueue():
    # 目前看这个队列是阻塞队列
    queue = Queue()
    p = Process(target=provider,args=(queue,))
    c = Process(target=consumer,args=(queue,))
    p.start()
    c.start()

    time.sleep(5)

if __name__ == "__main__":
    basic_process()
    # 多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
    #concurrency_process()
    process_pool(3)
    test_subprocess()
    communicateWithQueue()
