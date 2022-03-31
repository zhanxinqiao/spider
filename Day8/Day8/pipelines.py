# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter

from Day8.items import Day8Item1,Day8Item2
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings
import pymysql
settings = get_project_settings()

class Day8Pipeline:


    def open_spider(self,spider):

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

    def __init__(self):
        # settings = get_project_settings()
        # self.host1=settings['MONGODB_HOST']
        # self.port1 = settings['MONGODB_PORT']
        # self.db_name1=settings['MONGODB_DBNAME']
        # client=pymongo.MongoClient(host=self.host1,port=self.port1)
        # db=client[self.db_name1]
    #     self.post=db[settings['MONGODB_DOCNAME']]
    # def __init__(self,databaseIp='127.0.0.1',databasePort=27017,user="admin",password="123456",mongodbName="my_test"):
    #     client=MongoClient(databaseIp,databasePort)
    #     self.db=client[mongodbName]
    #     self.db.authenticate(user,password)
    #
        self.client=pymongo.MongoClient(host=settings['MONGODB_HOST'],port=settings['MONGODB_PORT'])
        # self.client.admin.authenticate(settings['MONGODB_USER'],settings['MONGODB_PSW'])
        db=self.client[settings['MONGODB_DBNAME']]
        self.coll=db[settings['MONGODB_COLL']]



    def process_item(self, item, spider):
        if isinstance(item,Day8Item1):
            print(item['name'],item['price'],item['link'])
            sql = 'insert into aa(name,price,link) values("{}","{}","{}")'.format(
                item['name'],item['price'],item['link']
            )
            self.cursor.execute(sql)
            self.conn.commit()
            return item

        elif isinstance(item,Day8Item2):
            print("item中的:")
            print(item['photo'])
            # postItem=dict(item)
            # self.coll.insert_one(postItem)
            self.coll.insert_many([{'name':item['name'],'photo':item['photo']}])
            return item




    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        self.client.close()
