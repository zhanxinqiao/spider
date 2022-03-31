import re
import time

import scrapy

from Day14.items import Day14Item,Day14Item2

class FalooSpider(scrapy.Spider):
    name = 'faloo'
    allowed_domains = ['www.hongxiu.com']
    start_urls = ['https://www.hongxiu.com/rank/hotsales/']

    def parse(self, response):
        link = []
        title = Day14Item()
        name_list = response.xpath(
            '//div[@class="book-mid-info"]//h4/a/text()').extract()
        link_list = response.xpath(
            '//div[@class="book-mid-info"]//h4/a/@href').extract()
        summary_list=response.xpath('//div[@class="book-mid-info"]//p[@class="intro"]/text()').extract()
        # https://b.faloo.com/1066177.html
        #https://www.hongxiu.com/book/16792364604322104
        for i in range(len(name_list)):
            print(name_list[i])
            link.append("https://www.hongxiu.com"+link_list[i])
            print(link_list[i])
            title['name'] = name_list[i]
            title['link'] = "https://www.hongxiu.com"+link_list[i]
            summary = re.findall(r'([\u4e00-\u9fa5].*)', summary_list[i])[0]
            title['summary']=summary
            yield scrapy.Request(url="https://www.hongxiu.com"+link_list[i], callback=self.parse_faloo)
            time.sleep(3)
            yield title

    def parse_faloo(self, response):
        desc = Day14Item2()
        desc['name'] = response.xpath('//div[@class="book-info"]/h1/em/text()').extract_first()
        desc['photo'] = response.xpath('//div[@class="book-information cf"]//div[@class="book-img"]/a/img/@src').extract_first()
        #https://bookcover.yuewen.com/qdbimg/349573/c_16792364604322104/180
        print(desc['photo'])
        yield desc
