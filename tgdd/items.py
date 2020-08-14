# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TgddItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    comment = scrapy.Field()
    brand = scrapy.Field()
    phone = scrapy.Field()
