# -*- coding: utf-8 -*-
import re

import scrapy

from fang.items import XFItem, ESFItem


class SfwSpider(scrapy.Spider):
    name = 'sfw'
    allowed_domains = ['fang.com']
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        global xfUrl
        global esfUrl
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            tds = tr.xpath(".//td[not(@class)]")
            province_text = tds[0].xpath(".//strong/text()").get()
            if province_text:
                province_text = re.sub(r'\s', "", province_text)
                if province_text:
                    province = province_text
            city_links = tds[1].xpath(".//a")
            for link in city_links:
                city_name = link.xpath("./text()").get()
                city_url = link.xpath("./@href").get()
                url_module = city_url.split("//")[1].split(".")
                if city_name == "北京":
                    # 新房链接
                    xfUrl = "http://newhouse.fang.com/house/s/"
                    # 二手房链接
                    esfUrl = "http://esf.fang.com/"
                else:
                    # 新房链接
                    xfUrl = "http://" + url_module[0] + ".newhouse.fang.com/house/s/"
                    # 二手房链接
                    esfUrl = "http://" + url_module[0] + ".esf.fang.com/"
                yield scrapy.Request(url=xfUrl, callback=self.parse_xf, meta={"info": (province, city_name, xfUrl)})

                yield scrapy.Request(url=esfUrl, callback=self.parse_esf, meta={"info": (province, city_name, esfUrl)})

    def parse_xf(self, response):

        province, city, baseUrl = response.meta["info"]
        lis = response.xpath("//div[@class='nl_con clearfix']//li")

        for li in lis:
            name = li.xpath(".//div[@class='house_value clearfix']/div[@class='nlcd_name']/a/text()").get()
            if name:
                name = name.strip()
            tmp = list(map(lambda x: x.replace("\t", ""),
                           li.xpath(".//div[@class='house_type clearfix']/a//text()").getall()))
            rooms = list(filter(lambda x: x.endswith("居"), tmp))
            size = "".join(li.xpath(".//div[@class='house_type clearfix']//text()").getall()).strip()
            size = re.sub(r"\s|/", "", size).split("－")
            if len(size) > 1:
                size = size[1].strip()
            address = li.xpath(".//div[@class='relative_message clearfix']//a/@title").get()
            if address:
                address = address.strip()
            status = li.xpath(".//div[@class='fangyuan']/span/text()").get()
            if status:
                status = status.strip()
            price = "".join(li.xpath(".//div[@class='nhouse_price']/text()").getall()).strip()
            price = re.sub(r"\s|广告", "", price)
            district = li.xpath(
                ".//div[@class='relative_message clearfix']//a/span[@class='sngrey']/text()").get()
            if district:
                district = district.strip()
            origin_url = li.xpath(".//div[@class='nlcd_name']/a/@href").get()
            if origin_url:
                origin_url = "https:"+origin_url.strip()
            item = XFItem(province=province, city=city, name=name, rooms=rooms, size=size, address=address,
                          status=status, price=price, district=district, origin_url=origin_url)
            yield item
        next = response.xpath("//div[@class='page']//a[@class='next']/@href").get()
        if next:
            next_url = baseUrl + next.split("/")[3]
            yield scrapy.Request(url=next_url, callback=self.parse_xf, meta={"info": (province, city, baseUrl)})

    def parse_esf(self, response):
        province, city, baseUrl = response.meta["info"]
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            name = dl.xpath(".//p[@class='add_shop']/a/@title").get()
            if name:
                name = name.strip()
            address = dl.xpath(".//p[@class='add_shop']/span/text()").get()
            if address:
                address = address.strip()
            tmp = dl.xpath(".//p[@class='tel_shop']/text()").getall()
            year = None
            if tmp:
                if '独栋' in tmp[0]:
                    rooms = "独栋"
                    size = tmp[3]
                    if size:
                        size = size.strip()
                    toward = tmp[4]
                    if toward:
                        toward = toward.strip()
                else:
                    rooms = tmp[0]
                    if rooms:
                        rooms = rooms.strip()
                    size = tmp[1]
                    if size:
                        size = size.strip()
                    floor = tmp[2]
                    if floor:
                        floor = floor.strip()
                    toward = tmp[3]
                    if toward:
                        toward = toward.strip()
                    if len(tmp) > 4:
                        year = tmp[4]
                        if year:
                            year = year.strip()

            price = "".join(dl.xpath(".//dd[@class='price_right']/span[@class='red']//text()").getall()).strip()
            unit = dl.xpath(".//dd[@class='price_right']/span[not(@class)]/text()").get()
            if unit:
                unit = unit.strip()
            origin_url =  dl.xpath(".//dt[@class='floatl']/a/@href").get()
            if origin_url:
                origin_url = baseUrl+origin_url.strip()
            item = ESFItem(province=province, city=city, name=name, price=price, size=size, rooms=rooms,
                           address=address, unit=unit, toward=toward, year=year, floor=floor, origin_url=origin_url)
            yield item
        next = response.xpath("//div[@class='page_al']//p")
        current_page = response.xpath("//div[@class='page_al']//span[@class='on']/text()").get().strip()
        if int(current_page) < int(next[-1].xpath("./text()").get().strip().replace("共", "").replace("页", "")):
            next_url = baseUrl + next[-3].xpath("./a/@href").get()
            yield scrapy.Request(url=next_url, callback=self.parse_xf, meta={"info": (province, city, baseUrl)})
