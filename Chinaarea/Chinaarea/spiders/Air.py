# -*- coding: utf-8 -*-
import scrapy

from Chinaarea.items import ChinaareaItem


class AirSpider(scrapy.Spider):
    name = 'Air'
    allowed_domains = ['aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/']
    base_url = 'https://www.aqistudy.cn/historydata/'

    def parse_day(self, response):
        print('爬取最终数据')
        item = ChinaareaItem()
        node_list = response.xpath('//tr')
        node_list.pop(0)
        for node in node_list:
            item['City'] = response.meta['city']
            item['Data'] = node.xpath('./td[1]/text()').extract_first()
            item['AQI'] = node.xpath('./td[2]/text()').extract_first()
            item['Level'] = node.xpath('./td[3]/span/text()').extract_first()
            item['PM2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['PM10'] = node.xpath('./td[5]/text()').extract_first()
            item['SO2'] = node.xpath('./td[6]/text()').extract_first()
            item['CO'] = node.xpath('./td[7]/text()').extract_first()
            item['NO2'] = node.xpath('./td[8]/text()').extract_first()
            item['O3'] = node.xpath('./td[9]/text()').extract_first()
            yield item

    def parse_datil(self, response):
        print('正在爬取城市具体信息')
        url_list = response.xpath('//tr/td/a/@href').extract()
        for url in url_list:
            link = self.base_url + url
            yield scrapy.Request(url=link,callback=self.parse_day,meta={
                'city':response.meta['city']
            })


    def parse(self, response):
        print('正在爬取所有城市信息')
        url_list = response.xpath('//div[@class="all"]/div[@class="bottom"]//a/@href').extract()
        # print(url_list)
        title_list = response.xpath('//div[@class="all"]/div[@class="bottom"]//a/text()').extract()
        # print(title_list)
        for url, city in zip(url_list, title_list):
            link = self.base_url + url
            yield scrapy.Request(url=link, callback=self.parse_datil, meta={
                'city': city
            })




