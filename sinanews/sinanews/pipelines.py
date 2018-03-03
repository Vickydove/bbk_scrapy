# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinanewsPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        self.dbpool = dbpool

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
    def process_item(self, item, spider):
        try:
            # 查重处理
            self.cursor.execute(
                """select * from sina where link = %s""",
                item['link'])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                pass
            else:
                # 插入数据
                self.cursor.execute(
                    # insert into sina(text, title, link, editor , date, source, keywords)
                    # value (%s, %s, %s, %s, %s, %s, %s)
                    (item['text'],
                     item['title'],
                     item['link'],
                     item['editor'],
                     item['date'],
                     item['source'],
                     item[' keywords']))
                # 提交sql语句
                self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
