# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

import functools

int2 = functools.partial(int, base=10)

print(int2("22222222",base=8))


max2 = functools.partial(max,100)
print(max2(*[1,3,5,7]))


# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
# 返回一个新的函数，调用这个新函数会更简单,当然调用新函数的时候也可以覆盖某些参数的默认值。

