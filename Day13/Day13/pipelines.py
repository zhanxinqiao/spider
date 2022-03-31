# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import pymysql
from itemadapter import ItemAdapter

from Day13.items import Day13Item,Day13Item2
from scrapy.utils.project import get_project_settings
settings = get_project_settings()

class Day13Pipeline:

    def open_spider(self,spider):
        self.conn=pymysql.Connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='test')
        self.cursor=self.conn.cursor()

    def __init__(self):

        self.client=pymongo.MongoClient(host=settings['MONGODB_HOST'],port=settings['MONGODB_PORT'])
        db=self.client[settings['MONGODB_DBNAME']]
        self.coll=db[settings['MONGODB_COLL']]



    def process_item(self, item, spider):
        if isinstance(item,Day13Item):
            print(item['name'],item['link'])
            sql = 'insert into yuedu(name,link) values("{}","{}")'.format(
                item['name'],item['link']
            )
            self.cursor.execute(sql)
            self.conn.commit()
            return item

        elif isinstance(item,Day13Item2):
            print(item['describe'])
            # postItem=dict(item)
            # self.coll.insert_one(postItem)
            self.coll.insert_many([{'name':item['name'],'photo':item['photo'],'describe':item['describe']}])
            return item




    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        self.client.close()
