# 用生产者消费者模式下载表情包
import os
import queue
import re
import threading
from urllib import request

import requests
from lxml import etree

tasks = queue.Queue(16)
urls = ["https://www.doutula.com/photo/list/?page=1",
        "https://www.doutula.com/photo/list/?page=2",
        "https://www.doutula.com/photo/list/?page=3",
        "https://www.doutula.com/photo/list/?page=4",
        "https://www.doutula.com/photo/list/?page=5",
        "https://www.doutula.com/photo/list/?page=6",
        "https://www.doutula.com/photo/list/?page=7"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
lock = threading.Lock()
empty = threading.Condition(lock)
full = threading.Condition(lock)

def putTaskIntoQueue(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    page = resp.text
    images = etree.HTML(page).xpath("//div[@class='page-content text-center']//img[@class != 'gif']")
    for image in images:
        img_url = image.xpath("@data-original")[0]
        alt = image.xpath("@alt")[0]
        alt = re.sub(r'[\?？\.，。！!\*]', "", alt)
        suffix = os.path.splitext(img_url)[1]
        task = {
            "name": alt + suffix,
            "url": img_url
        }
        lock.acquire()
        if tasks.full():
            full.wait()
        tasks.put(task)
        empty.notifyAll()
        lock.release()
    print("%s 完成图片收集工作..." % threading.currentThread().name)


def downloadImage():
    while True:
        lock.acquire()
        while tasks.empty():
            empty.wait()
        task = tasks.get()
        full.notifyAll()
        print(task)
        request.urlretrieve(task["url"], "D:/ep/uploads/images/" + task["name"])
        lock.release()


def main():
    global urls
    index = 1
    for url in urls:
        thread = threading.Thread(name="爬取线程" + str(index), target=putTaskIntoQueue, args=(url,))
        thread.start()
        index += 1
    index = 1
    for i in range(5):
        thread = threading.Thread(name="下载图片线程" + str(index), target=downloadImage)
        thread.start()
        index += 1


if __name__ == '__main__':
    main()
