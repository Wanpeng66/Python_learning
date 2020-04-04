# 爬取电影天堂前7页电影详细信息
import queue
import threading

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
Dongmans = []
urls = queue.Queue()


def getHtmlFromRemote(url, headers=None):
    resp = requests.get(url, headers=headers,verify=False)
    resp.encoding = resp.apparent_encoding
    return resp.text


def putUrltoQueue(page):
    html = etree.HTML(page)
    tables = html.xpath("//div[@class='bd3']//div[@class='co_content8']/ul/table")
    for table in tables:
        href = table.xpath(".//a/@href")  # 动漫详情页链接
        urls.put(href)


def getDongman(url):
    resp = requests.get(url, headers=headers,verify=False)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    title = html.xpath("//div[@class='title_all//font']")[0].get_text()
    detail = html.xpath("//div[@class='co_content8']//div[@id='Zoom']//tbody//a")[0]
    xlzz = detail.xpath("@yzthlmxc")
    mz = detail.xpath("@thunderrestitle")
    dongman = {
        "mz":mz,
        "xlzz":xlzz
    }
    return dongman


def getDetail():
    while True:
        url = urls.get()
        if url == "none":
            break
        dm = getDongman(url)
        print(dm)
        Dongmans.append(dm)


if __name__ == "__main__":
    subThread = threading.Thread(target=getDetail,name="爬取动漫详情页线程")
    subThread.start()
    for i in range(7):
        index = i + 1
        url = "https://www.dytt8.net/html/dongman/list_16_" + str(index) + ".html"
        page = getHtmlFromRemote(url, headers=headers)
        putUrltoQueue(page)
    urls.put("none")
    subThread.join()
