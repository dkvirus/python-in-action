import pymysql.cursors

class MariadbPipeline(object):

    # 批量存数据缓存区
    list = []

    # 批量存数据，一次最多存多少条数据
    max_count = 20

    # 一进入 MySQLPipeline 管道，连接数据库
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='47.98.171.103',   # 数据库地址
            port=13306,             # 数据库端口
            db='dkvirus',           # 数据库名
            user='dkvirus',         # 数据库用户名
            passwd='dkvirus123',    # 数据库密码
            charset='utf8',         # 编码方式
            use_unicode=True)
        self.cursor = self.conn.cursor()

    # 实现父类方法
    def process_item(self, item, spider):
        # 接收爬虫程序送过来的数据
        self.list.append([item['title'], item['desc'], item['time'], item['price'], item['post']])

        if len(self.list) == self.max_count:
            self.bulk_insert_to_mysql()
            # 清空缓冲区
            del self.list[:]
        return item

    # 批量存数据
    def bulk_insert_to_mysql(self):
        try:
            sql = "insert into yuanjisong (`title`, `desc`, `time`, `price`, `post`) values (%s, %s, %s, %s, %s)"
            self.cursor.executemany(sql, self.list)
            self.conn.commit()
        except:
            self.conn.rollback()

    # 离开该管道时，关闭相关流
    def close_spider(self, spider):
        self.bulk_insert_to_mysql()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()