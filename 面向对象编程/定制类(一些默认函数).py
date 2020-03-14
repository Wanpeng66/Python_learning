# 一些预定义函数的试用
class special(object):
    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__ : 类比于java中的toString方法
    def __str__(self):
        return "这是一个定制类..."

    # __iter__: 迭代器方法，该方法返回一个迭代对象
    # Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
    # 直到遇到StopIteration错误时退出循环
    def __iter__(self):
        return self

    def __next__(self):
        self.age = self.age + 1
        if self.age > 200:
            raise StopIteration("现在还没有活到200岁的人呢")
        return self.age

    # __getitem__ :按址访问，就是拿到指定下标的元素
    # 这种实现只能传下标，不能传切片表达式
    def __getitem__(self, item):
        return self.age+item

    # 正常情况下，当我们调用类的方法或属性时，
    # 如果不存在，编译器会默认调用__getattr__方法来尝试获取
    # 注意，只有在没有找到属性的情况下，才调用__getattr__，
    # 已有的属性，不会在__getattr__中查找
    # 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
    def __getattr__(self, item):
        if item == "addr":
            return "shanghai"
        elif item == "getScore":
            return lambda x : x*x

    # 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
    def __call__(self, *args, **kwargs):
        print("这是call方法...")


if __name__ == '__main__':
    sp = special("aa", 25)
    # 打印一个实例时，会默认打印返回__str__方法的返回值
    print(sp)

    # 对实例进行遍历时，会调用__item__方法返回的迭代对象的__next__方法
    for age in sp:
        print(age)

    # 此时会调用实例的__getitem__方法
    print(sp[1])

    # 实例中没有addr属性，会调用__getattr__方法来尝试获取
    print(sp.addr)
    # 实例中没有getScore方法，会调用__getattr__方法来尝试获取
    print(sp.getScore(2))
    # 定义了__call__方法，可以直接调用对象
    sp()
