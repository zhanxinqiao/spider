# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day8Item1(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    link=scrapy.Field()


class Day8Item2(scrapy.Item):
    name=scrapy.Field()
    photo = scrapy.Field()