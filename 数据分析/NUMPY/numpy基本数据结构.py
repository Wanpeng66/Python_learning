import numpy as np


def task1():
    arr = np.array([1, 2, "3", "hello", [4, 5, 6], {"name": "wp"}])
    print(arr)
    print(arr.shape)
    # 如果初始化数组的数据的数据类型不一致，如果包含字符串，则全部变为字符串，否则变成优先级高的
    l1 = [0, 1, 2, 3, 4, 5]
    # l2 = ["a", "b", "c", "d", "e", "f"]
    l3 = [True, False, True, False, True, False]
    arr = np.array([l1, l3])
    print(arr)
    print(arr.shape)


def task2():
    print(np.linspace(5, 15, num=10, endpoint=False, dtype=np.int))


def task3():
    print(np.zeros((4, 4)))
    print(np.ones((2, 3)))
    print(np.eye(3, 3))


def homework():
    task1()
    task2()
    task3()


if __name__ == '__main__':
    # 数组类型
    # 一维数组
    arr = np.array([1, 2, 3, 4])
    print(arr)

    # 这是二维数组 2行4列
    arr = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
    print(arr)
    # arr.ndim 表示此数组的纬度 二维数组就是2 三维数组就是3
    print(arr.ndim)
    # arr.shape 表示此数组的形状 几行几列
    print(arr.shape)
    # 数组中全部元素的个数
    print(arr.size)
    # 数组中元素的类型
    print(arr.dtype)

    # 这是三维数组 两个及以上二维数组组成，更高维数组以此类推
    arr = np.array([[[1, 2, 3], [1, 2, 3]], [[2, 3, 4], [2, 3, 4]]])
    print(arr)
    print(arr.shape)
    print(arr.size)

    # np.arange()方法：类似于range()，在给定间隔内返回均匀间隔的值
    print(np.arange(5))  # [0 1 2 3 4]
    print(np.arange(1, 10))  # [1 2 3 4 5 6 7 8 9]
    print(np.arange(2.1, 10))  # [2.1 3.1 4.1 5.1 6.1 7.1 8.1 9.1]
    print(np.arange(4, 20, 5))  # 5为步长 [ 4  9 14 19]

    # np.linspace()方法: 返回在间隔[开始，结束]上计算的num个均匀间隔的样本
    # 在10到20的21个元素之间，返回20个均匀间隔的数据
    print(np.linspace(10, 20, num=20))
    # endpoint参数标识是否将上限包含进来，默认为true,如果为false，则不包含
    print(np.linspace(11, 20, num=20, endpoint=False))
    # retstep是否返回步长，如果为true，则返回一个元组，第一个元素为实际数组，第二个元素为步长
    print(np.linspace(11, 20, num=20, retstep=True))

    # zeros()/zeros_like()
    # zeros()返回一个指定形状以及指定数据类型(默认为float)的数组，并用0填充
    print(np.zeros((4,)))
    print(np.zeros((2, 3)))
    print(np.zeros((2, 1, 2), dtype=np.int))
    arr = np.array([[2, 4, 6], [1, 3, 9]])
    print("--------------------")
    # zeros_like() 返回一个跟指定数组相同形状的数组，并用0填充
    print(np.zeros_like(arr))
    # ones()/ones_like() 与zeros()/zeros_like()相同，只是填充1
    print(np.ones((2, 3, 5), dtype=np.int))

    # eye():返回一个m*n的矩阵，对角线元素为1，其余元素为0,k标识对角线元素的偏移量
    print(np.eye(3, 4))
    print(np.eye(3, 5, k=5))

    # 作业
    homework()
