import re
import time

import scrapy

from Day11.items import Day11Item,Day11Item2


class XinbakeSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.laikan.com']
    start_urls = ['http://www.laikan.com/books']

    def parse(self, response):
        link = []
        title=Day11Item()
        name_list = response.xpath('//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/text()').extract()
        link_list = response.xpath('//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/@href').extract()
        #//book.qidian.com/info/1209977/
        #https://book.qidian.com/info/1209977/
        for i in range(len(name_list)):
            title = Day11Item()
            print(name_list[i])
            link.append("https:" + link_list[i])
            print("https:" + link_list[i])
            title['name'] = name_list[i]
            title['link'] = "https:" + link_list[i]
            yield scrapy.Request(url="https:"+link_list[i], callback=self.parse_b)
            yield title

    def parse_b(self, response):
        desc = Day11Item2()
        desc['name']=response.xpath('//div[@class="book-information cf"]//h1/em').extract_first()
        photo = response.xpath('////div[@class="book-img"]//img/@src').extract()[0]
        print(photo)
        desc['photo']="https:"+photo
        #//bookcover.yuewen.com/qdbimg/349573/1209977/180
        #https://bookcover.yuewen.com/qdbimg/349573/1209977/180
        describe1= response.xpath('//div[@class="left-wrap fl"]//div[@class="book-intro"]//p/text()').extract()[0]
        describe11=re.findall(r'([\u4e00-\u9fa5].*)', describe1)
        print(describe11)
        describe2 = response.xpath('//div[@class="left-wrap fl"]//div[@class="book-intro"]//p/text()').extract()[1]
        describe22 = re.findall(r'([\u4e00-\u9fa5].*)', describe2)
        print(describe22)
        desc['describe']=describe11[0]+describe22[0]
        print(desc['describe'])
        yield desc

