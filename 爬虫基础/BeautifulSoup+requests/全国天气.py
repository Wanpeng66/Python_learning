# 爬取全国当天天气情况
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}
weathers = []


def getHtmlFromRemote(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding
    return resp.text


def getCommonWeather(page):
    soup = BeautifulSoup(page, features="lxml")
    conMidtab2 = soup.find("div", attrs={'class': 'hanml'}).find_all("div", attrs={'class': "conMidtab2"})

    for con in conMidtab2:
        trs = con.find_all("tr")[2:]
        index = 0
        for tr in trs:
            tds = tr.find_all("td")
            if index == 0:
                city = list(tds[1].stripped_strings)[0]
                max_temp = list(tds[4].stripped_strings)[0]
                min_temp = list(tds[7].stripped_strings)[0]
            else:
                city = list(tds[0].stripped_strings)[0]
                max_temp = list(tds[3].stripped_strings)[0]
                min_temp = list(tds[6].stripped_strings)[0]
            weather = {
                "city": city,
                "max_temp": max_temp,
                "min_temp": min_temp
            }
            weathers.append(weather)
            index += 1


def getGATWeather(page):
    soup = BeautifulSoup(page, features="html5lib")
    hanml = soup.find("div", attrs={"class": "hanml"})
    conMidtab = hanml.find("div", attrs={"class": "conMidtab"})
    conMidtab2 = conMidtab.find("div", attrs={"class": "conMidtab2"})
    tables = conMidtab2.find_all("table")
    index = 0
    for table in tables:
        print(type(table))
        if index < 2:
            tds = table.find_all("tr")[2].find_all("td")
            city = list(tds[1].stripped_strings)[0]
            max_temp = list(tds[4].stripped_strings)[0]
            min_temp = list(tds[7].stripped_strings)[0]
            weather = {
                "city": city,
                "max_temp": max_temp,
                "min_temp": min_temp
            }
            weathers.append(weather)
        else:
            trs = table.find_all("tr")[2:]
            rowIndex = 0
            for tr in trs:
                tds = tr.find_all("td")
                if rowIndex == 0:
                    city = list(tds[1].stripped_strings)[0]
                    max_temp = list(tds[4].stripped_strings)[0]
                    min_temp = list(tds[7].stripped_strings)[0]
                else:
                    city = list(tds[0].stripped_strings)[0]
                    max_temp = list(tds[3].stripped_strings)[0]
                    min_temp = list(tds[6].stripped_strings)[0]
                weather = {
                    "city": city,
                    "max_temp": max_temp,
                    "min_temp": min_temp
                }
                weathers.append(weather)
                rowIndex += 1
        index += 1


if __name__ == "__main__":
    urls = ["http://www.weather.com.cn/textFC/hb.shtml",
            "http://www.weather.com.cn/textFC/db.shtml",
            "http://www.weather.com.cn/textFC/hd.shtml",
            "http://www.weather.com.cn/textFC/hz.shtml",
            "http://www.weather.com.cn/textFC/hn.shtml",
            "http://www.weather.com.cn/textFC/xb.shtml",
            "http://www.weather.com.cn/textFC/xn.shtml",
            "http://www.weather.com.cn/textFC/gat.shtml"]
    index = 0
    for url in urls:
        page = getHtmlFromRemote(url)
        if index != 7:
            getCommonWeather(page)
        else:
            getGATWeather(page)
        index += 1
    weathers.sort(key=lambda data: data["max_temp"], reverse=True)
    cities = map(lambda data: data["city"], weathers)
    max_temp = map(lambda data: data["max_temp"], weathers)
    bar = Bar("2020/4/5号中国气温最高的10个城市")
    bar.add("", cities, max_temp)
    bar.render("D:/ep/uploads/temperature.html")
