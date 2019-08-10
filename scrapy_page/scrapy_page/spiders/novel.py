import scrapy

class NovelSpider(scrapy.Spider):

    name = "novel"

    start_urls = ["https://www.biquge5200.cc/0_857/651708.html"]

    def parse(self, response):
        title = response.css('div.bookname h1::text').extract_first()
        content = '\n\n'.join(response.css('div#content p::text').extract())
        next_url = response.css('.bottem1 a::attr(href)').extract()[3]

        print("正在写入", title)
        with open('novel.txt', 'a') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
            f.write('\n\n')

        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)