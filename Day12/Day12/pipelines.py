# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
import pymysql

from Day12.items import Day12Item, Day12Item2

settings = get_project_settings()



class Day12Pipeline:
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
    #     self.conn=pymysql.Connect(host='localhost',port=3306,user='root',password='123456',charset='utf8',db='test')
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
        if isinstance(item,Day12Item):
            print(item['name'],item['link'])
            sql = 'insert into qidian(name,link) values("{}","{}")'.format(
                item['name'],item['link']
            )
            self.cursor.execute(sql)
            self.conn.commit()
            return item

        elif isinstance(item,Day12Item2):
            print("item中的:")
            print(item['name'])
            # postItem=dict(item)
            # self.coll.insert_one(postItem)
            self.coll.insert_many([{'name':item['name'],'photo':item['photo'],'describe':item['describe']}])
            return item




    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
        self.client.close()
