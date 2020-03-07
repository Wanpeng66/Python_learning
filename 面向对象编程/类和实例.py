# python中的类与实例与java中差不多 只不过写法不一样

# 用class关键字声明这是一个类，Student是类名，括号里可以写父类
# python不是静态语言 类的属性不固定 可以随时增删，所以声明类时不用声明属性，
# 一个类的不同实例可能也有不同的属性参数
class Student(object):
    # __init__是构造函数
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 不能有多个重写的构造器
    #def ___init__(self):
        #self = self

    # 可以定义方法
    def test(self):
        print("test....")



stu = Student("wp",25)
stu.test()

stu2 = Student()
stu2.test()

