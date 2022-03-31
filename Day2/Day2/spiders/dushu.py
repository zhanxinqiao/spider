import scrapy
from Day2.items import Day2Item

class DushuSpider(scrapy.Spider):
    name = 'dushu'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107.html']

    base_url='https://www.dushu.com/book/1107_'
    page=1
    def parse(self, response):
        nl_list=response.xpath('//div[@class="bookslist"]//li')
        for nl in nl_list:
            name=nl.xpath('.//h3/a/text()').extract_first()
            link=nl.xpath('.//h3/a/@href').extract_first()
            author=nl.xpath('.//p[1]/text()').extract_first()
            present=nl.xpath('.//p[2]/text()').extract_first()
            state=nl.xpath('.//p[3]/span/text()').extract_first()
            print(name+"的链接为："+link+author+present+state)
            book=Day2Item(name=name,link=link,author=author,present=present,state=state)
            yield book

        if self.page<10:
            self.page=self.page+1
            url=self.base_url+str(self.page)+'.html'
            print(url)
            yield scrapy.Request(url=url,callback=self.parse)
