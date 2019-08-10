import scrapy

class NovelSpider(scrapy.Spider):

    name = "novel"

    start_urls = ["https://www.biquge5200.cc/0_857/651708.html"]

    def parse(self, response):
        title = response.css('div.bookname h1::text').extract_first()
        content = '\n\n'.join(response.css('div#content p::text').extract())
        
        # 保存为本地文件 novel.txt
        with open('novel.txt', 'w') as f:
            f.write(title)
            f.write('\n')
            f.write(content)
        self.log('保存文件成功')