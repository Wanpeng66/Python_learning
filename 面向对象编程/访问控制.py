
class Student(object):
    # 类属性 类比java
    attr = "attr"
    def __init__(self,name,age):
        # 实例属性 类比java
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self,name):
        self.__name = name


stu = Student("wp",25)
# 如果一类的属性命名以__(双下划线)开头，则相当于被声明为私有属性，不能被外部直接访问，
# 如果要访问，可以和java一样提供getset方法
# 但是python没有直接硬性手段去控制访问，全凭自觉
# 还有一类属性以__开头，并以__结尾，这种属于特殊属性
# 特殊属性是可以直接访问的，不是private属性，所以，不能用__name__、__score__这样的属性名
#print(stu.__name)
print(stu.getName())



