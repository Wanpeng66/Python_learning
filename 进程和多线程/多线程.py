# Python的标准库提供了两个模块：_thread和threading，
# _thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
import threading


def thread_run(k):
    print("%s is running" % (threading.current_thread().name))
    while k < 5:
        k += 1
        print("%s >>> %s" % (threading.currentThread().getName(), k))
    print("end...")

balance = 0
lock = threading.Lock()
def changeBalance(n):
    global  balance
    lock.acquire()
    balance += n
    balance -= n
    lock.release()

def concurrency_run(n):
    for i in range(1000000):
        changeBalance(n)






if __name__ == "__main__":
    global k
    k = 0
    print('thread %s is running...' % threading.current_thread().name)
    # 新建线程和新建进程差不多
    t = threading.Thread(name="子线程1", target=thread_run, args=(k,))
    t.start()
    t.join()
    print('thread %s is end...' % threading.current_thread().name)

    t1 = threading.Thread(name="取钱线程1",target=concurrency_run,args=(100,))
    t2 = threading.Thread(name="取钱线程2",target=concurrency_run,args=(100,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)