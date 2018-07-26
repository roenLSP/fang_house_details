# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):

    name = scrapy.Field()
    local = scrapy.Field()
    name = scrapy.Field()
    total_price = scrapy.Field()
    price = scrapy.Field()
    chaoxiang = scrapy.Field()
    size = scrapy.Field()
    building_time = scrapy.Field()
    house_type =scrapy.Field()
    building_type =scrapy.Field()
    beizhu =scrapy.Field()
    school =scrapy.Field()

