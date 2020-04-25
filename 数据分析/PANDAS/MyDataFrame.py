# dataframe是pandas的二维数组类型
import numpy as npy
import pandas as pd

if __name__ == '__main__':
    # dataframe创建方式一： 由数组或列表组成的字典初始化
    # 字典的key会变成列名，index索引默认为从0开始的数字
    # 字典的元素个数一定要一致
    a = {"x": npy.random.rand(4), "y": npy.random.randn(4)}
    d = pd.DataFrame(a)
    print(d)
    b = {"i": [1, 2, 3], "j": [4, 5, 6]}
    d = pd.DataFrame(b)
    print(d)

    # columns参数是指定列的顺序，如果有的列数组中没有，则填充NaN
    d = pd.DataFrame(a, columns=["y", "x", "z"])
    print(d)

    # index参数是指定索引的（默认是从0开始的整数），且索引的个数必须跟数组中行数一致
    d = pd.DataFrame(a, index=["w", "a", "n", "p"])
    print(d)

    # 创建方法二：由series初始化

    c = {"x": pd.Series(npy.random.rand(3)), "y": pd.Series(npy.random.randn(3))}
    d = pd.DataFrame(c)
    print(d)

    # 由series初始化来的dataframe，colnums为字典的key，index为series的index(没指定的话就是整数)
    # series的长度可以不一样，没有的话会用NaN填充
    f = {"x": pd.Series(npy.random.rand(2), index=["a", "b"]),
         "y": pd.Series(npy.random.randn(3), index=["a", "b", "c"])}
    d = pd.DataFrame(f)
    print(d)

    # 创建方法三：由二维数组直接创建
    arr = npy.arange(9).reshape(3, 3)
    d = pd.DataFrame(arr)
    print(d)
    d = pd.DataFrame(arr, index=["a", "b", "c"], columns=["x", "y", "z"])
    print(d)

    # 创建方法四：由字典列表初始化
    p = [{"a": 10, "b": 20}, {"a": 60, "b": 70, "c": 0}]
    d = pd.DataFrame(p, index=["x", "y"])
    print(d)

    print("---------------------------")
    # dateframe的索引
    df = pd.DataFrame(npy.arange(12).reshape((3, 4)), index=["a", "b", "c"], columns=["x", "y", "z", "w"])
    print(df)
    # 直接写索引，默认是按列取
    d1 = df["y"]
    # 只取一列则返回一个series(一维数组)
    print(d1, type(d1))
    print("------------------")
    # 取多列则返回一个子dataframe
    d2 = df[["z", "w"]]
    print(d2, type(d2))
    print("-----------------")
    # 按行取值
    d3 = df.loc["a"]
    # 如果只取一行，那么会变成series，然后列名变index
    print(d3, type(d3))
    print("---------------")
    # 如果取多行，则返回一个子dataframe
    d4 = df.loc[["b", "c"]]
    print(d4, type(d4))
    print("---------------")
    # .iloc[] 是按行的下标进行取值，支持切片
    d5 = df.iloc[1:3]
    print(d5, type(d5))
