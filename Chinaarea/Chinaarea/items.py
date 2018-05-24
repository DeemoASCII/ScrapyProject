# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaareaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #城市
    City = scrapy.Field()
    #日期
    Data = scrapy.Field()
    #AQI空气质量指数
    AQI = scrapy.Field()
    #空气质量等级
    Level = scrapy.Field()
    #PM2.5
    PM2_5 = scrapy.Field()
    #PM10
    PM10 = scrapy.Field()
    #二氧化硫
    SO2 = scrapy.Field()
    #一氧化碳
    CO = scrapy.Field()
    #二氧化氮
    NO2 = scrapy.Field()
    #臭氧
    O3 = scrapy.Field()
    #数据源
    Source = scrapy.Field()
    #utctime
    Utc_time = scrapy.Field()

