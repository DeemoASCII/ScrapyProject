# -*- coding: utf-8 -*-
import scrapy

a = '//p[@class="status"]/text()'

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    # allowed_domains = ['http://www.renren.com']
    # start_urls = ['http://http://www.renren.com/']
    #
    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'

        yield scrapy.FormRequest(url=url,formdata={
            'email':'18988037324',
            'password':'400810520'
        },callback=self.parse)

    def parse(self, response):
        name = response.xpath(a).extract_first()
        with open('renren.txt','w') as f:
            f.write(name)