# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors

class MariadbPipeline(object):

    # 批量存数据缓存区
    chapterList = []

    # 批量存数据，一次最多存多少条数据
    max_count = 50

    # 一进入 MySQLPipeline 管道，连接数据库
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',   # 数据库地址
            port=3306,          # 数据库端口
            db='novel',         # 数据库名
            user='root',        # 数据库用户名
            passwd='',          # 数据库密码
            charset='utf8',     # 编码方式
            use_unicode=True)
        self.cursor = self.conn.cursor()

    # 实现父类方法
    def process_item(self, item, spider):
        # 接收爬虫程序送过来的数据
        self.chapterList.append([item['title'], item['url']])

        if len(self.chapterList) == self.max_count:
            self.bulk_insert_to_mysql()
            # 清空缓冲区
            del self.chapterList[:]
        return item

    # 批量存数据
    def bulk_insert_to_mysql(self):
        try:
            sql = "insert into chapter (`title`, `url`) values (%s, %s)"
            self.cursor.executemany(sql, self.chapterList)
            self.conn.commit()
        except:
            self.conn.rollback()

    # 离开该管道时，关闭相关流
    def close_spider(self, spider):
        self.bulk_insert_to_mysql()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


