# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem
class TaobaoscrapySpider(scrapy.Spider):
    name = "taobaoScrapy"
    allowed_domains = ["tmail.com"]
    start_urls = ['https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12576468ddANeb&q=%C4%D0%D7%B0&sort=s&style=g&active=2&industryCatId=all&type=pc']

    def parse(self, response):
        print(response)
        divs=response.xpath("//div[@class='product item-1111']/div[@class='product-iWrap']/")
        for div in divs:
            item=TaobaoItem()
            #商品价格
            item["goods_price"]=div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            item["goods_name"]=div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            pre_goods_url=div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item["goods_url"]=pre_goods_url if "http:" in pre_goods_url else ("http:"+pre_goods_url)
            yield scrapy.Request(url=item["goods_url"],meta={'item':item},callback=self.parse_detail)
    def parse_detail(self,response):
        div=response.xpath("//div[@class='name']/")
        item=response.meta['item']
        div=div[0]
        item["shop_name"]=div.xpath("a/text()")[0].extract()
        yield item


