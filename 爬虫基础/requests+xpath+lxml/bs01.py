
import random
import re
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def method1():
    url = "https://morvanzhou.github.io/static/scraping/basic-structure.html";
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, features="lxml")
    print(html.h1)
    print(html.p)
    a = html.find_all("a")
    for i in a:
        print(i["href"])


def method2():
    url = "https://morvanzhou.github.io/static/scraping/list.html"
    res = requests.get(url=url)
    html = BeautifulSoup(res.text, features="lxml")
    for tag in html.find_all("li", {"class": "month"}):
        print(tag.get_text())


def method3():
    url = "https://morvanzhou.github.io/static/scraping/table.html"
    res = requests.get(url)
    html = BeautifulSoup(res.text, features="lxml")
    images = html.find_all("img", {"src": re.compile(".*?\.jpg")})
    for img in images:
        print(img["src"])
    a = html.findAll("a", {"href": re.compile("https://morvan.*")})
    for i in a:
        print(i.get_text())


if __name__ == "__main__":
    #  method1()
    #  method2()
    #  method3()
    baseUrl = "https://baike.baidu.com"
    his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
    for i in range(20):
        res = requests.get(baseUrl + his[-1]).text
        html = BeautifulSoup(res, "lxml")
        print("title:%s,url:%s" % (html.find("h1").get_text(), his[-1]))
        print("-------------------------------------")
        sub_urls = html.find_all("a",
                                 {"target": "_blank", "href": re.compile("^/item/(%.{2})+$")})
        if len(sub_urls) > 0:
            his.append(random.sample(sub_urls, 1)[0]["href"])

