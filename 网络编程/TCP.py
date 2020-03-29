# socket
import socket

# socket客户端代码
import threading
from datetime import time


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.sina.com.cn", 80))
    # 发送数据:
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收数据:
    buffer = []
    while True:
        # 每次最多接收1k字节:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    # 关闭连接:
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('C:/Users/14793/Pictures/sina.html', 'wb') as f:
        f.write(html)


if __name__ == "__main__":
    client()
