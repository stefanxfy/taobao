# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem
class TaobaoscrapySpider(scrapy.Spider):
    name = "taobaoScrapy"
    allowed_domains = ["taobao.com"]
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
