# python中的dict类型(用{}括起来) 是键值对集合 相当于java中的map
score = {"wp":100,"wlj":90,"lhy":50}
print(score["wp"])

score["undefined"] = 10
print(score["undefined"])

if __name__ == '__main__':
    print(score.keys())
    print(score.values())
    print(score.items())