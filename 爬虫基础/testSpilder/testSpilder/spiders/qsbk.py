# -*- coding: utf-8 -*-
import scrapy


class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        divs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for div in divs:
            author = div.xpath("./div[@class='author clearfix']//h2/text()").get().strip()
            content = div.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            dz = {
                "author": author,
                "content": content
            }
            yield dz
