# 一般静态语言，需要在运行前就定义好class，然后运行期间加载class进行实例化对象
# 但是python是动态语言，可以在运行期动态生成class，然后再根据动态生成的class实例化对象
# 实例化class 有两种方法
# type()
# type()函数可以查看一个类型或变量的类型，也可以创建出新的类型

# type()方法可以动态生成class
# 但是生成的class的属性和方法相对固定，可以通过meteclass来动态修改class
# 举个例子：给一个类动态新增add方法
class MyMetaclass(type):
    # cls 就是要生成的那个对象
    # name 就是class的名字
    # bases 就是这个class的父类集合
    # attrs 就是class的属性和方法集合
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, x: x
        return type.__new__(cls, name, bases, attrs)


class TestMetaclass(object, metaclass=MyMetaclass):
    def __init__(self, val):
        self.val = val


if __name__ == "__main__":
    def hel(self):
        print("hello world")


    # 通过type()方法动态生成了一个Hello类，然后再实例化对象
    Hello = type("Hello", (object,), {"name": "aa", "hello": hel})
    # 要创建一个class对象，type()函数依次传入3个参数：
    # 1. class的名称；
    # 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    # 3. class的方法名称与函数绑定，以及属性与属性值的绑定，
    # 这里我们把函数hel绑定到方法名hello上，将aa赋值给name属性。
    a = Hello()
    print(a.name)
    a.hello()

    test = TestMetaclass("11")
    print(test.add(33))
    # metaclass其他用法还是自己查吧 一般用不到
