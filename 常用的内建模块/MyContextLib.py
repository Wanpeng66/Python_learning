# 上下文类库
'''
在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。
正确关闭文件资源的一个方法是使用try...finally：
    try:
        file = open("xxxx","r")
        file.read()
    finally:
        file.close()

写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，
所以上面的代码可以简化为:
    with open("xxx","r") as f:
       f.read()
不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的,例如下面的Test类

但是编写__enter__和__exit__仍然很繁琐,因此contextlib提供了更简单的写法:@contextmanager

'''
from contextlib import contextmanager, closing
from urllib.request import urlopen


class Test(object):
    def __init__(self,name):
        self._name = name

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")

    def query(self):
        print('Query info about %s...' % self._name)

class Test2(object):
    def __init__(self,name):
        self._name = name

    def query(self):
        print('Query info about %s...' % self._name)

# @contextmanager这个decorator接受一个generator，
# 用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
@contextmanager
def creat_query(name):
        print("start...")
        test2 = Test(name)
        yield test2
        print("end...")

# 如果我们希望在目标方法执行前，执行一些特定的行为，也可以使用@contextmanager来实现,类似aop
@contextmanager
def tag(name):
    print("start...")
    yield
    print("end...")

if __name__ =="__main__":
    with Test("wp") as t:
        t.query()
    with creat_query("wp") as test2:
        test2.query()
    with tag("wp"):
        print("目标方法执行...")

    # 如果不想使用@contextmanager，也可以使用closing()来把该对象变为上下文对象
    with closing(urlopen("http://www.baidu.com")) as page:
        for line in page:
            print(line)
