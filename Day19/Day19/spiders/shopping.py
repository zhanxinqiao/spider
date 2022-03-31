import scrapy


class ShoppingSpider(scrapy.Spider):
    name = 'shopping'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['https://www.amazon.cn/s?i=specialty-aps&srs=1478512071&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&pf_rd_i=1841388071&pf_rd_m=A1U5RCOVU0NYF2&pf_rd_p=17db0adf-8870-4c0c-873f-4b78c0afd356&pf_rd_r=BDYZXNWV62TGXBASP156&pf_rd_s=merchandised-search-top-4&pf_rd_t=101&ref=nb_sb_noss']

    def parse(self, response):
        name_list = response.xpath(
            '//div[@class="s-main-slot s-result-list s-search-results sg-row"]//div[@class="a-section a-spacing-none"]/h2/a/span/text()').extract()
        link_list = response.xpath('//div[@class="s-main-slot s-result-list s-search-results sg-row"]//div[@class="a-section a-spacing-none"]/h2/a/@href').extract()
        for i in range(len(name_list)):
            print(name_list[i]+"的链接："+link_list[i])
