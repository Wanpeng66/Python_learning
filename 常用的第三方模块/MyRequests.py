# 第三方url类库 使用更方便
import requests


# get方法
def getMethod():
    res = requests.get("https://www.douban.com/search", params={"q": "python", "cat": "1001"})
    print(res.url)
    res = requests.get("https://www.douban.com/",timeout=2.5)
    print(res.status_code)
    print(res.text)

# post方法
def postMethod():
    url = "https://accounts.douban.com/login"
    # requests默认使用application/x-www-form-urlencoded对POST数据编码。
    res = requests.post(url, data={'form_email': 'abc@example.com', 'form_password': '123456'})

    # 如果要传递JSON数据，可以直接传入json参数,内部自动序列化为JSON
    res = requests.post(url, json={'form_email': 'abc@example.com', 'form_password': '123456'})

    # 上传文件需要更复杂的编码格式，但是requests把它简化成files参数
    # 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度
    upload_file = {"file": open("C:/Users/14793/Pictures/剑姬.jpeg", "rb")}
    res = requests.post(url, files=upload_file)
    print(res.headers)
    print(res.cookies)


if __name__ == "__main__":
    getMethod()
    postMethod()
