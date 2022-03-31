# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
import pymysql
class Day2Pipeline:
    def open_spider(self,spider):
        settings=get_project_settings()
        self.host=settings['DB_HOST']
        self.port=settings['DB_PORT']
        self.user=settings['DB_USER']
        self.password=settings['DB_PASSWORD']
        self.name=settings['DB_NAME']
        self.charset=settings['DB_CHARSET']
        self.connect()

    def connect(self):
        self.conn=pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor=self.conn.cursor()

    def process_item(self, item, spider):
        sql='insert into book(name,link,author,present,state) values("{}","{}","{}","{}","{}")'.format(
            item['name'],item['link'],item['author'],item['present'],item['state']
        )
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()