import time

import scrapy

from Day16.items import Day16Item, Day16Item2


class DoubandushuSpider(scrapy.Spider):
    name = 'doubandushu'
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/latest?tag=%E5%85%A8%E9%83%A8/']

    def parse(self, response):
        link = []
        book1 = Day16Item()
        name_list = response.xpath(
            '//ul[@class="chart-dashed-list"]//div[@class="media__body"]/h2/a/text()').extract()
        author_list = response.xpath(
            '//ul[@class="chart-dashed-list"]//p[@class="subject-abstract color-gray"]/text()').extract()
        link_list = response.xpath('//ul[@class="chart-dashed-list"]//div[@class="media__img"]/a/@href').extract()
        for i in range(len(name_list)):
            print(name_list[i])
            print(author_list[i])
            #https://book.douban.com/subject/35671232/
            link.append(link_list[i])
            print(link_list[i])
            book1['name'] = name_list[i]
            book1['author'] = author_list[i]
            book1['link'] = link_list[i]
            # yield scrapy.Request(url=link_list[i], callback=self.parse2)
            yield book1
    #
    # def parse2(self, response):
    #     book2 = Day16Item2()
    #     name = response.xpath('//div[@class="subject clearfix"]//a/img/@alt').extract_first()
    #     photo = response.xpath('//div[@class="subject clearfix"]//a/img/@src').extract_first()
    #     print(photo)
    #     book2['name'] = name
    #     book2['photo'] = photo
    #     yield book2