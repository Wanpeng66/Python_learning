# 跟java枚举差不多的功能
from enum import Enum, unique

# @unique装饰器会检查枚举类中有没有重复的值
@unique
class Weekday(Enum):
    Sun = 7
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


if __name__ == "__main__":
    # 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
    print(Weekday.Sun)
    print(Weekday(2))
    print(Weekday.Sun.value)