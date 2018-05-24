# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 回答数
    answer_count = scrapy.Field()
    # 文章数
    articles_count = scrapy.Field()
    # 头像
    avatar_url = scrapy.Field()
    # 关注者
    follower_count = scrapy.Field()
    # 签名
    headline = scrapy.Field()
    # id
    id = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 主业地址
    url = scrapy.Field()
    # url_token
    url_token = scrapy.Field()
    # 用户类型
    user_type = scrapy.Field()
