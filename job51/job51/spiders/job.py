# -*- coding: utf-8 -*-
import scrapy

from job51.items import Job51Item


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?']

    def parse(self, response):
        node_list = response.xpath('//*[@id="resultList"]/div[@class="el"]')
        next_page = response.xpath('//div[@class="p_in"]/ul/li/a/@href').extract()
        for node in node_list:
            item = Job51Item()
            detail_link = node.xpath('./p/span/a/@href').extract_first()
            item['position_name'] = node.xpath('./p/span/a/@title').extract_first()
            item['company'] = node.xpath('./span[1]/a/@title').extract_first()
            item['work_address'] = node.xpath('./span[2]/text()').extract_first()
            item['salary'] = node.xpath('./span[3]/text()').extract_first()
            item['publishtime'] = node.xpath('./span[4]/text()').extract_first()
            yield scrapy.Request(url=detail_link, callback=self.parse_detail, meta={
                'item': item,
            })
        for url in next_page:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['content'] = response.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()').extract()
        item['contact'] = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()[1:][0][:-7]
        yield item
