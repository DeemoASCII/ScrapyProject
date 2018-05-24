# -*- coding: utf-8 -*-
import time

import scrapy

from Elara.items import ElaraItem


class TanzhouSpider(scrapy.Spider):
    name = 'tanzhou'
    allowed_domains = ['tanzhouedu.com']
    start_urls = ['http://www.tanzhouedu.com/mall/course/initAllCourse']
    offset = 0

    def parse(self, response):
        item = ElaraItem()
        node_list = response.xpath('//*[@id="newCourse"]/div/div/ul/li')
        for node in node_list:
            item['money'] = node.xpath('./div/span/text()').extract_first()
            item['title'] = node.xpath('./a/@title').extract_first()
            yield item

        if node_list == []:
            return None
        else:
            self.offset += 20
            yield scrapy.Request(
                url='http://www.tanzhouedu.com/mall/course/initAllCourse?params.offset={}&params.num=20&keyword=&_={}'.format(
                    str(self.offset), str(int(time.time() * 1000))), callback=self.parse)


