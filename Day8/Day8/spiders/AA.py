import time
import scrapy
from Day8.items import Day8Item1

from Day8.items import Day8Item2


class AaSpider(scrapy.Spider):
    name = 'AA'
    allowed_domains = ['mall.masadora.net']
    start_urls = ['https://mall.masadora.net/?size=64&categoryId=54']

    def parse(self, response):
        link=[]
        shop = Day8Item1()
        name_list=response.xpath('//div[@class="home_product-list__2FH2V"]//div[@class="product_product-name__1wAJ0"]/text()').extract()
        price_list=response.xpath('//div[@class="home_product-list__2FH2V"]//span[@class="product_product-money-count__VFNB_"]/text()').extract()
        link_list=response.xpath('//div[@class="home_product-list__2FH2V"]/a/@href').extract()
        for i in range(len(name_list)):
            print(name_list[i])
            print(price_list[i])
            link.append("https://mall.masadora.net"+link_list[i])
            print("https://mall.masadora.net"+link_list[i])
            shop['name']=name_list[i]
            shop['price']=price_list[i]
            shop['link']="https://mall.masadora.net"+link_list[i]
            yield scrapy.Request(url="https://mall.masadora.net"+link_list[i], callback=self.parse2)
            time.sleep(3)
            yield shop


    def parse2(self,response):
        shop2 = Day8Item2()
        name=response.xpath('//div[@class="productDetail_goods-title__13UC5"]/@title').extract_first()
        photo=response.xpath('//div[@class="productDetail_cover__1AVEG"]/img/@src').extract_first()
        print(photo)
        shop2['name'] = name
        shop2['photo']=photo
        yield shop2
