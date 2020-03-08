# property注解简化了属性的声明和getset

class Animal(object):
    # 把一个get方法变成属性声明，并返回一个装饰器 @name
    # 对外暴露的属性名为方法名，切记方法名与实际属性名不能一样，否则栈溢出
    # 下面例子就对外暴露一个name属性，实际属性名为__name
    @property
    def name(self):
        return self.__name

    # name装饰器有很多子方法，有setter，getter等等
    @name.setter
    def name(self, value):
        self.__name = value

if __name__ == '__main__':
    pig = Animal()
    # 上面定义的name属性，可以直接实例.属性名来调用
    pig.name = "wp"
    print(pig.name)

