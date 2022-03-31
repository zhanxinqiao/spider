import scrapy
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('baidu')
        name_list=response.xpath('//div[@id="s-top-left"]/a/text()').extract()
        src_list = response.xpath('//div[@id="s-top-left"]/a/@href').extract()
        for i in range(len(name_list)):
            print(name_list[i]+"的链接是"+src_list[i])
