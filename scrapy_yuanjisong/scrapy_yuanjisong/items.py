import scrapy

class ScrapyYuanjisongItem(scrapy.Item):
    title = scrapy.Field()      # 标题
    desc = scrapy.Field()       # 描述
    time = scrapy.Field()       # 时间
    price = scrapy.Field()      # 价格
    post = scrapy.Field()       # 投递人数
