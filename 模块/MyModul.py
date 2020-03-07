"这是模块"
__author__ = "wp"
# 上面两句是模块的注释，第一行是模块的说明，第二行是作者的说明
# 模块顾名思义，定义方法，定义变量，然后供别人调用
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def main():
    print("main..............")

# 以_或__开头的方法或变量为私有方法和私有变量
# Python并没有一种方法可以完全限制访问private函数或变量，
# 但是，从编程习惯上不应该引用private函数或变量
def _personl():
    print("私有方法...")

# 这么写相当于java中的main方法
if __name__ == "__main__":
    test()
    main()

