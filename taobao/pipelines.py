# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TaobaoPipeline(object):
    def __init__(self):
        self.num=0;
    def process_item(self, item, spider):
        print(self.num+1)
        return item
