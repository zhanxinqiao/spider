# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from scrapy.utils.project import get_project_settings
from itemadapter import ItemAdapter
settings = get_project_settings()

class Day10Pipeline:
    def __init__(self):
        self.client=pymongo.MongoClient(host=settings['MONGODB_HOST'],port=settings['MONGODB_PORT'])
        # self.client.admin.authenticate(settings['MONGODB_USER'],settings['MONGODB_PSW'])
        db=self.client[settings['MONGODB_DBNAME']]
        self.coll=db[settings['MONGODB_COLL']]


    def process_item(self, item, spider):
        self.coll.insert_many([{'name': item['name'], 'photo': item['photo'],'title':item['title'],'describe':item['describe']}])
        return item

