# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    position_name = scrapy.Field()
    #职位类别
    position_type = scrapy.Field()
    #工作类型
    work_type = scrapy.Field()
    #工作地点
    work_address = scrapy.Field()
    #招聘人数
    recruitment_number = scrapy.Field()
    #发布时间
    release_time = scrapy.Field()
    #学历
    education = scrapy.Field()
    #工作年限
    working_years = scrapy.Field()
    #岗位描述
    job_description = scrapy.Field()
    #岗位要求
    job_requirements = scrapy.Field()
