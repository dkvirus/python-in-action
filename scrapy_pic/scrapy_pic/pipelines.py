from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ScrapyPicPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        '''
        把蜘蛛文件 yield 过来的图片地址列表进行下载
        '''
        for img_url in item['img_urls']:
            yield Request(img_url)

    def file_path(self, request, response=None, info=None):
        '''
        给图片重命名
        '''
        # 原路径：https://www.wangbase.com/blogimg/asset/201908/bg2019080702.jpg
        # 文件名取最后一部分 bg2019080702.jpg
        filename = request.url.split('/')[-1]
        return filename