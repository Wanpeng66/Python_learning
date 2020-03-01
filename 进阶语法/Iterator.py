# python只要是可迭代对象，无论有无下标，都可以迭代，比如list、dict、str
from collections import Iterable

tmp = [1, 2, 3]
for i in tmp:
    print(i)

# enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for k, v in enumerate(tmp):
    print(k, v)


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for val in d.values():
    print(val)
for k,v in d.items():
    print(k,v)


# 判断是否可迭代
isinstance('abc', Iterable)
