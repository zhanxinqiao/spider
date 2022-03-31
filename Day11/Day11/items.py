# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day11Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    link=scrapy.Field()

class Day11Item2(scrapy.Item):
    name = scrapy.Field()
    photo=scrapy.Field()
    describe=scrapy.Field()