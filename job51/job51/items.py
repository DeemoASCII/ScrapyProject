# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    position_name = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 工作地点
    work_address = scrapy.Field()
    # 薪资范围
    salary = scrapy.Field()
    # 发布时间
    publishtime = scrapy.Field()
    # 详情页内容
    content = scrapy.Field()
    # 联系方式
    contact = scrapy.Field()

    source = scrapy.Field()
    utc_time = scrapy.Field()
