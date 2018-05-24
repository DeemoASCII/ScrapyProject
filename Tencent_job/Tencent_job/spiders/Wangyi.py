# -*- coding: utf-8 -*-
import scrapy
from Tencent_job.items import TencentJobItem


class WangyiSpider(scrapy.Spider):
    name = 'Wangyi'
    allowed_domains = ['hr.163.com']
    start_urls = ['https://hr.163.com/position/list.do']
    next_page = 'https://hr.163.com/position/list.do?currentPage={}'

    def parse(self, response):
        item = TencentJobItem()
        i = 1
        node_list = response.xpath('//div[@class="main-wrap"]/table/tbody/tr')
        for node in node_list:
            if i % 2 == 1:
                item['position_name'] = node.xpath('./td[1]/a/text()').extract_first()
                item['position_type'] = node.xpath('./td[2]/text()').extract_first()
                item['work_type'] = node.xpath('./td[3]/text()').extract_first()
                item['work_address'] = node.xpath('./td[4]/text()').extract_first()
                item['recruitment_number'] = node.xpath('./td[5]/text()').extract_first()[66:68]
                item['release_time'] = node.xpath('./td[6]/text()').extract_first()
                i += 1
                continue
            else:
                item['education'] = node.xpath('./td/div/ul/li[1]/text()').extract_first()[-2:]
                item['working_years'] = node.xpath('./td/div/ul/li[2]/text()').extract_first()[1:]
                job_description = node.xpath('./td/div/div[1]/p/text()').extract()
                job_description[0] = job_description[0][45:]
                item['job_description'] = job_description
                job_requirements = node.xpath('./td/div/div[2]/p/text()').extract()
                job_requirements[0] = job_requirements[0][45:]
                item['job_requirements'] = job_requirements
                i += 1
                yield item
        for i in range(133):
            yield scrapy.Request(url=self.next_page.format(i),callback=self.parse)


