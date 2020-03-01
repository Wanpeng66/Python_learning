# Python内置的非常简单却强大的可以用来创建list的生成式

# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(range(1, 11))
print(l)


# 生成[1x1, 2x2, 3x3, ..., 10x10]
l = [ x*x for x in range(1,11)]
print(l)

# 还可以在for循环后加判断
# or循环后面还可以加上if判断，这样我们就可以筛选出非偶数的平方
l = [x*x for x in range(1,11) if x%2 != 0]
print(l)

# 还可以使用两层循环
l = [m+n for m in "ABC" for n in "XYZ"]
print(l)

# 迭代dict
d = {'x': 'A', 'y': 'B', 'z': 'C' }
l = [k+":"+v.lower() for k,v in d.items()]
print(l)


# 在for之前加if else
# 在一个列表生成式中，for前面的if ... else是表达式(对结果进行操作,相当于sql中的having子句)，
# 而for后面的if是过滤条件(相当于sql中的查询条件)，不能带else。
l = [x if x%2==0 else -x for x in list(range(1,11))]
print(l)

L = ['Hello', 'World', 18, 'Apple', None]
l = [s if not isinstance(s,str) else s.lower()  for s in L]
print(l)