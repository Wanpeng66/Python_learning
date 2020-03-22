#  datetime是Python处理日期和时间的标准库。
from datetime import datetime, timedelta, timezone

if __name__ =="__main__":
    # 1.获取当前日期和时间
    now = datetime.now()
    print(now)

    # 获取指定日期和时间
    date = datetime(2021,3,21,19,15)
    print(date)

    # datetime转换为timestamp
    date = datetime(2020,3,22,19,15)
    print(date.timestamp())

    # timestamp转换为datetime
    t = 1429417200.0
    # 默认按当前时区转换
    date = datetime.fromtimestamp(t)
    print("北京时间：",date)
    date = datetime.utcfromtimestamp(t)
    print("格林威治时间：",date)

    # str转换为datetime
    date = datetime.strptime("2015-6-1 18:19:59","%Y-%m-%d %H:%M:%S")
    print(date)

    # datetime转换为str
    now = datetime.now()
    print(now.strftime("%a, %b %d %H:%M"))

    # datetime加减
    now = datetime.now()
    print(now + timedelta(days=1))
    print(now - timedelta(hours=2))

    # 本地时间转换为UTC时间
    now = datetime.now()
    tz_utc_8 = timezone(timedelta(hours=8))
    now.replace(tzinfo=tz_utc_8)
    print(now.tzinfo)

    # 时区转换
    # 可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(utc_now)
    bj_now = utc_now.astimezone(tz=timezone(timedelta(hours=8)))
    print(bj_now)
    tokyo_now = bj_now.astimezone(tz=timezone(timedelta(hours=9)))
    print(tokyo_now)


