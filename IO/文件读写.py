# 顾名思义，对文件或file-like 对象的读写

if __name__ == "__main__":
    try:
        f = open("D:\Program Files\gitrepository\Python_learning\\resources\Io.txt",encoding="UTF-8")
        print(f.read())
    finally:
        f.close()

    # with语句自动调用close()方法
    with open("D:\Program Files\gitrepository\Python_learning\\resources\Io.txt",encoding="UTF-8") as f:
        print(f.readlines())

    with open("D:\Program Files\gitrepository\Python_learning\\resources\Io.txt","a",encoding="UTF-8") as f:
        f.writelines("\r\nhello world")
