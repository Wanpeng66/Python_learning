import numpy as npy


def homework2():
    arr = npy.arange(0, 20)
    print(arr.reshape((4, 5)))
    print(npy.resize(arr, (5, 6)))

    arr = npy.reshape(npy.arange(0, 16), (4, 4))
    print(arr.astype(str))

    arr = npy.reshape(npy.arange(0, 16), (4, 4))
    arr = arr * 10 + 100
    print(arr)
    print(arr.mean())
    print(npy.sum(arr, axis=0))
    print(npy.sum(arr, axis=1))

    arr = npy.reshape(npy.arange(25), (5, 5))
    print(arr)
    print(arr[4])
    print(arr[:2, 3:])
    print(arr[3][2])

    arr = npy.resize(npy.arange(9), (3, 3))
    print(arr)
    arr1 = npy.array(arr[arr >= 5])
    print(arr1)


if __name__ == '__main__':
    # 数组的变形方法 .T/.reshape()/.resize()
    arr1 = npy.arange(0, 5)
    # .T 方法是将数组反转
    # 如果是一维数组则不变
    print(arr1.T)
    arr1 = npy.ones((2, 3), dtype=npy.int)
    # 如果是二维数组，则由x行y列 ---> y行x列
    print(arr1.T)

    # reshape()方法是将给定数组变形为新的shape(变形前后，数组的size要一致，不然会报错)
    # npy.reshape((2,4)) == arr2.reshape((2,4)) 都会返回一个新的数组
    arr2 = npy.arange(1, 6)
    # print(arr2.reshape(2, 3))
    arr2 = npy.arange(1, 7)
    print(arr2.reshape((3, 2)))
    print(arr2)
    print("------------------------------>")
    arr2 = npy.zeros((3, 4), dtype=npy.int)
    print(arr2.reshape((6, 2)))
    print(arr2)

    # resize()方法也是将给定数组变形为新的shape，不过没有数组元素个数限制，多了剩，少了补
    # npy.resize(arr3,(3,2))会返回一个新数组，arr3.resize((3,2))会修改arr3
    arr3 = npy.arange(3, 7)
    print(npy.resize(arr3, (2, 4)))
    arr3 = npy.resize(arr3, (3, 2))
    print(npy.resize(arr3, (5, 5)))

    # 改变数组的元素类型 .astype()
    arr1 = npy.array(npy.arange(1, 8), dtype=float)
    print(arr1)
    arr2 = arr1.astype(npy.int64)
    print(arr2)

    homework2()
