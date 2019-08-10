import scrapy
from scrapy_yuanjisong.items import ScrapyYuanjisongItem

class YuanjisongSpider(scrapy.Spider):

    name = 'yuanjisong'

    start_urls = ['https://www.yuanjisong.com/job']

    def parse(self, response):
        panels = response.css('#db_adapt_id .weui_panel')
        item = ScrapyYuanjisongItem()

        for panel in panels:
            panel_bd = panel.css('.job_list_item_div .weui_panel_bd')
            
            item['desc'] = panel_bd[0].css('.media_desc_adapt::text').extract_first()   # 描述
            item['time'] = panel_bd[2].css('.media_desc_adapt span::text')[1].extract() # 时间
            item['price'] = panel_bd[3].css('.media_desc_adapt .rixin-text-jobs::text').extract_first() # 价格
            item['post'] = panel.css('.i_post_num::text').extract_first()      # 投递人数
            item['title'] = panel.css('.topic_title::text').extract_first()     # 标题
            
            yield item

        # 判断下一章 url 不为空，继续爬取
        next_url = response.css('.pagination li a::attr(href)')[-1].extract()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)