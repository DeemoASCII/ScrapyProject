# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import json
import redis

class ChinaPipeline(object):
    def process_item(self, item, spider):
        item['Source'] = spider.name
        item['Utc_time'] = str(datetime.datetime.utcnow())
        return item


class ChinaareaPipeline(object):

    def open_spider(self, spider):
        self.file = open('air.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()
