import re

import scrapy
from Day13.items import Day13Item,Day13Item2

class MotieSpider(scrapy.Spider):
    name = 'motie'
    allowed_domains = ['www.laikan.com']
    start_urls = ['http://www.laikan.com/books/']

    def parse(self, response):
        link = []
        title = Day13Item()
        name_list = response.xpath('//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/text()').extract()
        link_list = response.xpath('//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/@href').extract()
        # //book.qidian.com/info/1209977/
        # http://www.laikan.com/book/195134
        for i in range(len(name_list)):
            print(name_list[i])
            name=re.findall(r'([\u4e00-\u9fa5].*)',name_list[i])[0]
            link.append("http://www.laikan.com" + link_list[i])
            print("http://www.laikan.com" + link_list[i])
            title['name'] = name
            title['link'] = "http://www.laikan.com" + link_list[i]
            yield scrapy.Request(url="http://www.laikan.com" + link_list[i], callback=self.parse22)
            yield title

    def parse22(self, response):
        desc = Day13Item2()
        name = response.xpath('//div[@class="work_brief clearfixer"]//div[@class="title clearfixer"]/span[1]/text()').extract_first()
        desc['name']= re.findall(r'([\u4e00-\u9fa5].*)', name)[0]
        desc['photo']= response.xpath('//div[@class="work_brief clearfixer"]//div[@class="pic fl"]/span/img/@src').extract_first()
        # describe1 = response.xpath('//div[@class="left-wrap fl"]//div[@class="book-intro"]//p/text()').extract()[0]
        # describe11 = re.findall(r'([\u4e00-\u9fa5].*)', describe1)
        # print(describe11)
        # describe2 = response.xpath('//div[@class="left-wrap fl"]//div[@class="book-intro"]//p/text()').extract()[1]
        # describe22 = re.findall(r'([\u4e00-\u9fa5].*)', describe2)
        # print(describe22)
        # desc['describe'] = describe11[0] + describe22[0]
        desc['describe']=response.xpath('//div[@class="summary"]/pre/text()').extract_first()
        print(desc['describe'])
        yield desc
