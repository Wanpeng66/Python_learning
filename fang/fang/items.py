# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 新房item
class XFItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 单价
    price = scrapy.Field()
    # 面积
    size = scrapy.Field()
    # 几居室
    rooms = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 是否在售
    status = scrapy.Field()
    # 房天下页面地址
    origin_url = scrapy.Field()


class ESFItem(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 小区名字
    name = scrapy.Field()
    # 总价
    price = scrapy.Field()
    # 面积
    size = scrapy.Field()
    # 几居室
    rooms = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 单价
    unit = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 年代
    year = scrapy.Field()
    # 第几层
    floor = scrapy.Field()
    # 房天下页面地址
    origin_url = scrapy.Field()
