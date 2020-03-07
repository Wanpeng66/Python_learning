# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

def lazy_sum(*args):
    def sum():
        total = 0
        for arg in args:
            total += arg
        return total
    return sum
f = lazy_sum(1,3,5,7,9)
print(f())


# 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包（Closure）”
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())
# 上面返回的三个函数结果都是一样的
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# 如果一定要引用循环变量怎么办？
# 方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1(),f2(),f3())





# 如果函数内要使用全局变量，则必须在函数内用 global关键字来声明然后使用
# global关键字用来在函数或其他局部作用域中使用全局变量。
key = 0
def test():
    global key  # 声明使用key这个全局变量
    print(key)


test()  # 打印出0

# 如果函数想使用外部嵌套函数声明的局部变量，则必须用nonlocal关键字声明再使用
def createCounter():
    n=0
    def counter():
        nonlocal n   # 声明使用n这个局部变量
        n=n+1
        return n
    return counter

counter = createCounter()
print(counter(),counter(),counter())


L = list(filter(lambda n : n % 2 == 1,range(1,20)))
print(L)