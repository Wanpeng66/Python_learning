# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 跟java的装饰器模式类似 通过包装来增强功能


# 下面这个装饰器可以在执行目标方法前，打印日志
def metric(fn):
    def wrapper(*args, **kv):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kv)

    return wrapper

# 定义完装饰器之后，可以通过@符号标记在目标方法上
@metric
def log():
    print("log...")
log()

# 如果装饰器需要传递参数 则可以再嵌套一层
def log2(*text):
    def decorator(fn):
        def warpper(*args,**kv):
            print('%s executed in %s ' % (fn.__name__, text))
            res = fn(*args,**kv)
            print('post... ')
            return res
        return warpper
    return decorator

@log2("wp")
def now():
    print('2020/03/01')
now()

def time(fn):
    def warpper(*args,**kv):
        print("start time is 1111")
        r = fn(*args,**kv)
        print("end time is 2222")
        return r
    return warpper

@time
def q():
    print("now is 2020/03/07")

q()