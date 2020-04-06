# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WxappSpiderItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    content = scrapy.Field()


class MyImageItem(scrapy.Item):
    name = scrapy.Field()
    # scrapy自带的图片pipeline，规定item属性为：image_urls，images
    image_urls = scrapy.Field()
    images = scrapy.Field()
