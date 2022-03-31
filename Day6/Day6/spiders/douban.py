import scrapy


class DushuSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        nr_list=response.xpath('//ol[@class="grid_view"]//div[@class="hd"]')
        for nr in nr_list:
            name=nr.xpath('.//a/span[1]/text()').extract_first()
            src=nr.xpath('.//a/@href').extract_first()
            print(name+"的链接为"+'\t'+src)