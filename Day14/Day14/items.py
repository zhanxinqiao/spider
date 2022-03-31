# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day14Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    summary=scrapy.Field()

class Day14Item2(scrapy.Item):
    name = scrapy.Field()
    photo=scrapy.Field()
