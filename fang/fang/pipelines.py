# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

from fang.items import XFItem


class FangPipeline(object):
    def __init__(self):
        self.newhouse = open("D:/ep/uploads/xf.json", "wb")
        self.newhouse_exporter = JsonLinesItemExporter(self.newhouse, ensure_ascii=False)
        self.esf = open("D:/ep/uploads/esf.json", "wb")
        self.esf_exporter = JsonLinesItemExporter(self.esf, ensure_ascii=False)

    def process_item(self, item, spider):
        if isinstance(item, XFItem):
            self.newhouse_exporter.export_item(item)
        else:
            self.esf_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.newhouse.close()
        self.esf.close()
