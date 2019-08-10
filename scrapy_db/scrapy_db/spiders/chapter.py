import scrapy
from scrapy_db.items import ChapterItem

class ChapterSpider(scrapy.Spider):

    name = "chapter"

    start_urls = ["https://www.biquge5200.cc/0_857/"]

    def parse(self, response):
        # 看 html 源代码，第十个 dd 元素才是第一章节的内容
        dds = response.css('#list dd')[9:]
        item = ChapterItem()

        for dd in dds:
            item['title'] = dd.css('a::text').extract_first()
            item['url'] = dd.css('a::attr(href)').extract_first()
            yield item