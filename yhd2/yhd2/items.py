# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yhd2Item(scrapy.Item):
    productID = scrapy.Field()
    pmId = scrapy.Field()
    yhdprice = scrapy.Field()
    linkurl  = scrapy.Field()
    isYihaodian = scrapy.Field()
    name = scrapy.Field()
    categoryId = scrapy.Field()
    marketPrice = scrapy.Field()
    salePrice = scrapy.Field()
   # picUrl =scrapy.Field()
    productType =scrapy.Field()
    currentDate = scrapy.Field()

   # promEndDate = scrapy.Field()
   # promotionPoint = scrapy.Field()
   # rate = scrapy.Field()
   # recommend = scrapy.Field()
   # recommendType = scrapy.Field()
   # rule = scrapy.Field()
   # shoppingCount = scrapy.Field()
   # categoryName = scrapy.Field()
    #promotionId = scrapy.Field()