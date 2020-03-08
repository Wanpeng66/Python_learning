# python是动态语言，可以在类的声明之外给类或类的实例增加功能或属性
# 一般什么属性和方法都可以新增，但是这带来了很大的不确定性
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Person(object):
    # 相当于定义类的属性
    __slots__ = ("name","age","addr")
    # 全局属性count
    count = 0

    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.addr = addr

    def countIncr(self):
        # 如果使用类全局属性必须通过类型.属性名 使用
        Person.count += 1

class Wp(Person):
    __slots__ = Person.__slots__+("wname","wage")

    def __init__(self,name,age):
        self.wname = name
        self.wage = age



p = Person("wp",25,"anhuui")
# 下面给p实例增加tel属性则报错
#p.tel = "111111"
wp = Wp("wp",24)
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
wp.addr = "ah"
print(wp.addr)





