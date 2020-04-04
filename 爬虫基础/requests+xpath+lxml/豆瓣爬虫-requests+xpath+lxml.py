#  爬取豆瓣电影的数据
import requests

# 从远程连接获取页面
from lxml import etree


def getHtmlFromRemote(url, headers=None):
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    return html.text


def getMovies(page):
    movies = []
    html = etree.HTML(page)
    lis = html.xpath("//div[@id='upcoming']//ul[@class='lists']/li")
    for li in lis:
        title = li.xpath("@data-title")[0]
        region = li.xpath("@data-region")[0]
        director = li.xpath("@data-director")[0]
        actors = li.xpath("@data-actors")[0]
        thumbnail = li.xpath(".//img//@src")[0]
        movie = {
            "title": title,
            "region": region,
            "director": director,
            "actors": actors,
            "thumbnail": thumbnail
        }
        movies.append(movie)
    return movies


if __name__ == "__main__":
    url = "https://movie.douban.com/cinema/nowplaying/shanghai/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Referer": "https://movie.douban.com/"
    }
    page = getHtmlFromRemote(url, headers=headers)
    movies = getMovies(page)
    for movie in movies:
        print(movie)
