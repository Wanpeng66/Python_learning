# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 第一种generator,(***),括号以及括号内的表达式一起构成了一个generator对象
# 然后可以通过for循环来遍历generator 获得每一个元素
g = (s for s in list(range(1, 21)))
print(g)
for s in g:
    print(s)


# 第二种 通过函数来定义generator
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。
# 简而言之，有几个yield generator对象就有几个元素


# 杨辉三角
def triangles(max):
    n, L = 1, [1]

    while n <= max:
        yield L

        L1 = L + [0]

        L2 = [0] + L

        L = [L1[i] + L2[i] for i in range(len(L1))]

        n += 1

    return "done"


for s in triangles(10):
    print(s)
