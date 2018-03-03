# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SinanewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class textItem(Item):
    text = Field()        #文本正文
    title = Field()       #标题
    link = Field()        #链接
    editor = Field()      #责任编辑
    date = Field()        #日期
    source = Field()      #来源
    keywords = Field()    #关键字