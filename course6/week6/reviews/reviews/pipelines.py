# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class ReviewsPipeline(object):
    def process_item(self, item, spider):
        if item['text'] is None or len(item['text']) < 3:
            raise DropItem("null review")
        else:            
            return item
