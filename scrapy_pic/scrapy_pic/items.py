import scrapy


class ScrapyPicItem(scrapy.Item):
    img_urls = scrapy.Field()
