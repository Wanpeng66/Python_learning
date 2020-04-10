# python里的list集合类型(用[]括起来) 相当于java中的数组类型
classmates = ["wp","wlj"]
print(classmates.count("wp"))


# python中的tuple集合类型(用()括起来)，定义后元素不可变，只能查询
classmates = ("wp","wlj")

if __name__ == '__main__':
    hobbies = ["1","2","3","4"]
    hobbies.reverse()
    print(hobbies)
    hobbies.sort(reverse=True)
    print(hobbies)
    print(hobbies.count(2))
    # print(hobbies.index("5"))

    yz = (2,)
    print(yz)