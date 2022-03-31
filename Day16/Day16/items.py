# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Day16Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    link = scrapy.Field()

# class Day16Item2(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = scrapy.Field()
#     photo = scrapy.Field()