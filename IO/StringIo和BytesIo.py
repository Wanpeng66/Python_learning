# 顾名思义 就是在内存中字符串和字节缓冲区
# tip:
#    这两个缓冲区都维护了一个指针，write方法会移动指针到末尾，然后read方法就读到空的
#    需要将指针移动到相应位置再read，如果将指针移动到前面，进行write会覆盖前面的内容
#    然后指针会移动到末尾

from io import StringIO, BytesIO

if __name__ == "__main__":
    si = StringIO("qqqqqq\nwwwwww\n")
    # si.write("ssssss\n")
    # si.writelines(["aaaaa\n","vvvvvvv\n"])
    while True:
        str = si.readline()
        if str == "":
            break
        print(str.strip())

    # print(si.getvalue())

    bi = BytesIO()
    bi.write("中国".encode("UTF-8"))
    print(bi.getvalue())
    bi.seek(0,0)
    bi.write("fffff".encode("UTF-8"))
    # bi.seek(0,0)
    print(bi.read())
    print(bi.getvalue())