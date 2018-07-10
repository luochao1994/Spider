# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RenrenItem(scrapy.Item):
    collections = 'renrenche'

    car_code = scrapy.Field()
    img_src = scrapy.Field()
    title = scrapy.Field()
    carinfo = scrapy.Field()
    price = scrapy.Field()
    firstpay = scrapy.Field()
    type = scrapy.Field()
    city = scrapy.Field()

