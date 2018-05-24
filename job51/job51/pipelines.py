# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

import pymongo
import pymysql


class Job51Pipeline(object):
    # def open_spider(self, spider):
    #     self.file = open('job51.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        item['source'] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        # content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # self.file.write(content)
        return item
    #
    # def close_spider(self, spider):
    #     self.file.close()


class Job51MongoPipeline(object):

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.client['job51']['job51']

    def process_item(self, item, spider):
        # item['source'] = spider.name
        # item['utc_time'] = str(datetime.utcnow())
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class Job51MysqlPipeline(object):

    def open_spider(self, spider):
        self.con = pymysql.connect(host='localhost', port=3306, database='job51', user='root', password='400810')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        # item['source'] = spider.name
        # item['utc_time'] = str(datetime.utcnow())
        sql = (
            '''insert into job51(source,utctime,positionname,company,workaddress,salary,publishtime,content,contact) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
        list_item = [item['source'], item['utc_time'], item['position_name'], item['company'], item['work_address'],item['salary'], item['publishtime'], item['content'], item['contact']]
        self.cur.execute(sql, list_item)
        self.con.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.con.close()
