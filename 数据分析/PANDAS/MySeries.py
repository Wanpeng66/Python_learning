# Series是pandas的一维数组类型
# Series与numpy的一维数组相比，多了一个索引
# Series与dict类似，index是索引，value是一维数组的元素，不过Series更像一个有顺序的字典
import pandas as pd
import numpy as npy


def homework4():
    d = {"Jack": 90, "Marry": 92.0, "Tom": 89, "Zack": 65.0}
    s = pd.Series(d, name="homework1")
    print(s)
    print("-------------------")
    a = [90, 92.0, 89, 65.0]
    s = pd.Series(a, index=["Jack", "Marry", "Tom", "Zack"], name="homework1")
    print(s)
    print("-------------------")
    s = pd.Series(data=npy.random.rand(10)*100, index=list("abcdefghij"))
    print(s)
    print(s["b"])
    print(s["c"])
    print(s[3:6])
    # print([s[index] for index, val in s.items() if val > 50])
    print(s[s > 50])


if __name__ == '__main__':
    # Series创建方法一：由字典进行初始化，字典的key就是index，字典的value就是数组的元素
    d = {"a": 1, "b": 22, 3: 0}
    s = pd.Series(d)
    print(s)

    # Series创建方法二：由numpy的一维数组进行初始化，index默认为一维数组下标
    n = npy.random.rand(10)
    s = pd.Series(n)
    print(s)

    # Series创建方法三：通过标量创建 100为数组元素，index为数组索引 创建5个值为100的元素，索引从0到4
    s = pd.Series(100, index=range(5))
    print(s)
    print("-----------------")
    homework4()