import scrapy

from Day10.items import Day10Item


class FanqieSpider(scrapy.Spider):
    name = 'fanqie'
    allowed_domains = ['fanqienovel.com']
    start_urls = ['https://fanqienovel.com/rank?enter_from=menu/']

    def parse(self, response):
        link_list=response.xpath('//div[@class="muye-rank-book-list"]//div[@class="rank-book-item"]/button/a/@href').extract()
        print(link_list)
        for link in link_list:
            yield scrapy.Request(url="https://fanqienovel.com" +link, callback=self.parse2)

    def parse2(self, response):
        book = Day10Item()
        book['name'] = response.xpath('//div[@class="page-header"]//div[@class="info-name"]/h1/text()').extract_first()
        print(book['name'])
        photo= response.xpath('//div[@class="page-header"]//div[@class="book-cover loaded"]/img/@src').extract_first()
        print( photo)
        book['photo']="https:"+photo
        book['title']=response.xpath('//div[@class="page-header"]//div[@class="info-last"]//span/text()').extract()[0]
        book['describe']=response.xpath('//div[@class="page-body-wrap"]//div[@class="page-abstract-content"]/p/text()').extract_first()
        yield book

#//p3-tt.byteimg.com/img/pgc-image/8c8ede2baa26473a9ce2c3c3bf765d09~180x234.jpg
#https://p3-tt.byteimg.com/img/pgc-image/8c8ede2baa26473a9ce2c3c3bf765d09~180x234.jpg