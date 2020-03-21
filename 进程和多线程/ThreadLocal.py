# thradLocal:线程本地变量，与java思想差不多
import threading


student_local = threading.local()
def process_student():
    name = student_local.name
    age = student_local.age
    print("%s : %s : %s" %(threading.currentThread().getName(),name,age))

def process_thread(name,age):
    student_local.name = name
    student_local.age = age
    process_student()




if __name__ =="__main__":
    t1 = threading.Thread(name="线程1",target=process_thread,args=("alice",22))
    t2 = threading.Thread(name="线程2",target=process_thread,args=("bob",33))

    t1.start()
    t2.start()
    t2.join()
    t1.join()
