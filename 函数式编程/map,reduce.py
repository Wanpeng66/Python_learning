# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
from functools import reduce


def sqr(x):
    return x*x

l = list(range(1,10))
print(list(map(sqr,l)))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x,y):
    return x+y

print(reduce(add,l))


s = ['adam', 'LISA', 'barT']

def fm(m):
    return (str(s)[0].upper()+str(s)[1:].lower() for s in m)

print(list(fm(s)))

def prod(list):
    def cj(x,y):
        return x * y

    return reduce(cj,list)

print(prod([1,2,3]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
s = "1234.567"
def str2float(tmp):
    def char2num(s):
        return DIGITS[s]
    def ge(x,y):
        return x*10+y
    def le(x,y):
        return x*0.1+y

    index = str(tmp).index(".")
    t1 = tmp[0:index]
    t2 = "0"+tmp[index+1:]
    t1 = list(map(char2num,t1))
    t2 = list(map(char2num,t2))
    t2.reverse()
    print(reduce(ge,t1))
    print(reduce(le,t2))
    return reduce(ge,t1)+reduce(le,t2)

print(str2float(s))

print(1234567/1000)