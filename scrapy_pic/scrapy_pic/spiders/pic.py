import scrapy
from scrapy_pic.items import ScrapyPicItem

class PicSpider(scrapy.Spider):

    name = 'pic'

    start_urls = ['http://www.ruanyifeng.com/blog/2019/08/weekly-issue-68.html']

    def parse(self, response):
        img_urls = response.css("#main-content img::attr(src)").extract() 

        if img_urls:
            item = ScrapyPicItem()  
            item['img_urls'] = img_urls
            yield item