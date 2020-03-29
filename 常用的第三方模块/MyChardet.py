# 第三方编码类库，主要作用是检测编码
import chardet

if __name__ == "__main__":
    print(chardet.detect(b"wpwpwpwpwpw"))
    data = '离离原上草，一岁一枯荣'.encode('gbk')
    print(chardet.detect(data))
