# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TestspilderPipeline(object):
    # 运行一个新爬虫时会调用这个方法，完成一些准备工作，比如打开一个json文件，以供爬虫存储数据
    def __init__(self):
        self.duanzi = open("D:/ep/uploads/duanzis.json", "w", encoding="UTF-8")

    def open_spider(self, spider):
        print("糗事百科爬虫开始...")

    # 爬虫保存数据时会调用
    def process_item(self, item, spider):
        dz_json = json.dumps(dict(item),ensure_ascii=False)+"\\n"
        self.duanzi.write(dz_json)
        return item

    # 关闭一个爬虫时会调用
    def close_spider(self, spider):
        self.duanzi.close()
        print("关闭糗事百科爬虫...")
