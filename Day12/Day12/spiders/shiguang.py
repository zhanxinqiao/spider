import time

import scrapy

from Day12.items import Day12Item

from Day12.items import Day12Item2


class ShiguangSpider(scrapy.Spider):
    name = 'shiguang'
    allowed_domains = ['mtime.com']
    start_urls = ['http://list.mtime.com/listIndex/']

    def parse(self, response):
        link = []
        title=Day12Item()
        name_list = response.xpath('//div[@class="movie-item-list"]//div[@class="movie-item top-pic"]/a/@title').extract()
        link_list = response.xpath('//div[@class="movie-item-list"]//div[@class="movie-item top-pic"]/a/@href').extract()
        #http://movie.mtime.com/12231/
        for i in range(len(name_list)):
            print(name_list[i])
            link.append(link_list[i])
            print(link_list[i])
            title['name'] = name_list[i]
            title['link'] =link_list[i]
            yield scrapy.Request(url=link_list[i], callback=self.parse_link)
            time.sleep(3)
            yield title

    def parse_link(self, response):
        desc = Day12Item2()
        desc['name']=response.xpath('//div[@class="img_box"]/a/img/@alt').extract_first()
        desc['photo'] = response.xpath('//div[@class="img_box"]/a/img/@src').extract_first()
        print(desc['photo'])
        desc['describe'] = response.xpath('//div[@class="clearfix"]//p[@class="mt6 moreEllipsis"]/text()').extract()[0]
        print(desc['describe'])
        yield desc
