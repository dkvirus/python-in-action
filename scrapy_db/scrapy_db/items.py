# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ChapterItem(scrapy.Item):
    title = scrapy.Field()      # 章节标题
    url = scrapy.Field()        # 章节地址
