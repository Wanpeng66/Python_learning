# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp_spider.wxapp_spider.items  import MyImageItem


class WxspiderSpider(CrawlSpider):
    name = 'wxSpider'
    allowed_domains = ['wxapp-union.com']
    #  start_urls列表放置了爬虫启动后最先访问你的连接，默认是get请求访问
    #  如果想一开始发送post请求，比如登陆，则需要自己重写start_requests方法，如下所示
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+?mod=list&catid=2&page=\d'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'.+/article-.+\.html'),
             callback='parse_detail', follow=False)
    )

    # def start_requests(self):
    #     url = "xxxx"
    #     data={
    #         "username":"xxx",
    #         "password":"123"
    #     }
    #     request = scrapy.FormRequest(url=url,formdata=data,callback="parse_item",errback={})
    #     request = scrapy.Request(url=url,method="post",headers=[],body=[],callback={},errback={})
    #     yield request

    def parse_item(self, response):
        item = {}
        # name = response.xpath("//div[@class='tit_top wp cl']/h3/text()").get()
        # print(name)
        return item

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//p[@class='authors']/span/text()").get()
        content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(content).strip()
        urls = response.xpath("//div[@class='avatar_left cl']//img")
        url = urls[0].xpath("./@src").get()
        # item = WxappSpiderItem(title=title, author=author, pub_time=pub_time, content=content)
        image_item = MyImageItem(name=author, image_urls=[url])
        yield image_item
