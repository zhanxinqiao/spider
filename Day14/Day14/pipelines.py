# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import pymysql
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings

from Day14.items import Day14Item, Day14Item2

settings = get_project_settings()


class Day14Pipeline:
    def open_spider(self, spider):
    #         self.host=settings['DB_HOST']
    #         self.port=settings['DB_PORT']
    #         self.user=settings['DB_USER']
    #         self.password=settings['DB_PASSWORD']
    #         self.name=settings['DB_NAME']
    #         self.charset=settings['DB_CHARSET']
    #         self.connect()
    #
    # def connect(self):
    #         self.conn=pymysql.connect(
    #             host=self.host,
    #             port=self.port,
    #             user=self.user,
    #             password=self.password,
    #             db=self.name,
    #             charset=self.charset
    #         )
        self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', charset='utf8',
                                    db='test')
        self.cursor = self.conn.cursor()

    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        db = self.client[settings['MONGODB_DBNAME']]
        self.coll = db[settings['MONGODB_COLL']]

    def process_item(self, item, spider):
        if isinstance(item, Day14Item):
            print(item['name'], item['link'])
            sql = 'insert into faloo(name,link,summary) values("{}","{}","{}")'.format(item['name'], item['link'],
                                                                                        item['summary']
                                                                                        )
            # sql = """insert into faloo(name,link,describe) values(%s,%s,%s)"""
            # values = (pymysql.escape_string(item['name']),pymysql.escape_string(item['link']),
            #           pymysql.escape_string(item['link']))
            self.cursor.execute(sql)
            self.conn.commit()
            return item
        elif isinstance(item, Day14Item2):
            print(item['name'])
            self.coll.insert_many([{'name': item['name'], 'photo': item['photo']}])
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        self.client.close()
