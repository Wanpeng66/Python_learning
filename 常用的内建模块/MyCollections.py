# collections是Python内建的一个集合模块，提供了许多有用的集合类
import argparse
import os
from collections import deque, namedtuple, defaultdict, OrderedDict, ChainMap, Counter

if __name__ == "__main__":
    # namedtuple  命名的元组
    # namedtuple是一个函数，它用来创建一个自定义的tuple对象，
    # 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
    # 第一个参数是该namedtuple的名字，后面的数组是属性数组
    point = namedtuple("point", ["x", "y"])
    p = point(1, 2)
    print(p.x, p.y)

    # deque 双端队列
    q = deque(["a","b","c"])
    # 从队列尾插入
    q.append("d")
    print(q)
    # 从队列头插入
    q.appendleft("e")
    print(q)

    # defaultdict 带默认值的字典
    # 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
    dd = defaultdict(lambda:None)
    dd["key1"] = "val1"
    print(dd)
    # 对于不存在的键值对 返回默认值
    print(dd.get("key2"))

    # OrderedDict 有序的字典
    # 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
    od = OrderedDict()
    od["a"] = "a"
    od["c"] = "c"
    od["b"] = "b"
    print(od)

    # ChainMap 链式查找的字典
    # 例子：应用程序往往都需要传入参数,参数可以通过命令行传入,可以通过环境变量传入,还可以有默认参数
    # 可以用ChainMap实现参数的优先级查找,即先查命令行参数,如果没有传,再查环境变量,如果没有,就使用默认参数

    # 构造缺省参数:
    defaults = {
        'color': 'red',
        'user': 'guest'
    }
    # 构造命令行参数:
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = { k: v for k, v in vars(namespace).items() if v }

    # 组合成ChainMap: 前面的字典优先级高，先查
    combined = ChainMap(command_line_args, os.environ, defaults)
    # 打印参数:
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])

    # Counter
    # Counter是一个简单的计数器，例如，统计字符出现的个数
    c = Counter()
    c.update("hello world")
    print(c)

