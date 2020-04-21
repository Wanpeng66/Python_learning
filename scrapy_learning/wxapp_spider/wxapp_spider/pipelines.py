# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.exporters import JsonLinesItemExporter
from scrapy.pipelines.images import ImagesPipeline
from wxapp_spider.wxapp_spider import settings

# 存储页面数据为json文件



class WxappSpiderPipeline(object):
    def __init__(self):
        self.wxjc = open("D:/ep/uploads/wxjc.json", "wb")
        self.exporter = JsonLinesItemExporter(self.wxjc, ensure_ascii=False, encoding="UTF-8")

    def process_item(self, item, spider):
        print(spider)
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.wxjc.close()


# 下载图片的pipeline
class MyImagesPipeline(ImagesPipeline):

    # 发送图片请求前会调用此方法，可以在此方法中将item保存下来，可以在后面用
    def get_media_requests(self, item, info):
        requests = super(MyImagesPipeline, self).get_media_requests(item, info)
        for request in requests:
            request.item = item
        return requests

    # 保存图片时会调用此方法获取图片保存路径
    def file_path(self, request, response=None, info=None):
        file_path = super(MyImagesPipeline, self).file_path(request, response, info)
        category = request.item['name']
        store = settings.IMAGES_STORE
        true_path = os.path.join(store, category)
        if not os.path.exists(true_path):
            os.mkdir(true_path)
        name = file_path.replace("full/", "")
        return os.path.join(true_path, name)

    def process_item(self, item, spider):
        return item
