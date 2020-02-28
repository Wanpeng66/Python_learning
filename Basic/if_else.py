hige = 1.75
weight = 80.5
bmi = (weight/hige)**2
if bmi > 32:
    print("过于肥胖")
elif bmi <=32 & bmi>28:
    print("肥胖")
elif bmi<=28 & bmi >25:
    print("过重")
elif bmi <=25 & bmi >18.5:
    print("正常")
else:
    print("过轻")