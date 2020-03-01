# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# 定义自己的绝对值函数
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad type...")
    if int(x) > 0:
        return x
    else:
        return -x


# print(my_abs("ee"))


# 定义一个空函数
def non():
    pass


# 定义一个返回多个返回值的函数，angle为默认参数，不传时为0


def move(x, y, step, angle=0):
    nowX = x + step * math.cos(angle)
    nowY = y - step * math.sin(angle)
    return nowX, nowY


x, y = move(0, 0, 10)
print(x, y)


def quadratic(a, b, c):
    tmp = b * b - 4 * a * c
    if tmp < 0:
        raise EnvironmentError("别瞎几把传值...")
    x = (-b + math.sqrt(tmp)) / 2 * a
    y = (-b - math.sqrt(tmp)) / 2 * a
    return x, y


print(quadratic(4, 5, 1))


# 定义一个可变参数(参数任意传几个，可传可不传，可传2个也可传5个)的函数

def cal(*params):
    return len(params)


# 如果有list(可变数组)或tuple(不可变数组) 可以在前面放* 表示将数组拆成一个个参数
params = {4, 6, 7, 8}
print(cal(*params))


# 定义有关键字参数的函数，
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def key(x, y, **kw):
    print(x, y, kw)


key(1, 2, name="wp")
# 如果有现成的dict(map)集合 则可以加**来简化传参
user = {"name": "wp"}
key(1, 2, **user)


# 关键字参数可以丰富函数的功能，不过却不能限定关键字参数的key,调用者可能会乱传
# 所以可以使用命名关键字参数来限制可传入的关键字参数的key
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, addr, tel="110"):
    print(name, age, addr, tel)


# 此时addr和tel是必须要传的 如果不想必传可以设定默认值
person('Jack', 24, addr='Beijing')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def user(name, age, *scores, addr, tel="110"):
    print(name, age, scores, addr, tel)


scores = (22, 33, 44)
user("wp", 25, *scores, addr="sh")

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def product(*numbers):
    for number in numbers:
        if not isinstance(number,(int,float)):
            raise TypeError("参数中有非数字型参数...")
    sum = 1;
    for number in numbers:
        sum = sum * number
    return sum

print(product(3,4))