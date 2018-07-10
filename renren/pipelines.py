# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from renren.items import RenrenItem


class RenrenPipeline (object):

    def process_item(self, item, spider):
        return item


class PymongoRenrenPipeline (object):

    def __init__(self):

        conn = pymongo.MongoClient (host=settings['MONGODB_HOST'],
                                    port=settings['MONGODB_PORT'])
        db = conn[settings['MONGODB_DB']]
        self.collection = db[RenrenItem.collections]

    def process_item(self, item, spider):
        if isinstance (item, RenrenItem):
            self.collection.update ({'car_code': item['car_code']}, {'$set': item})

        return item
