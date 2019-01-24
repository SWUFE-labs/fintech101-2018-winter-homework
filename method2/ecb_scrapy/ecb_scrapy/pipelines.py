# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import EcbScrapyItem
from scrapy.conf import settings
import pymongo

class EcbScrapyPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[dbname]
        self.post = db[settings['MONGODB_COLLECTION_ECB']]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

# class FRScrapyPipeline(object):
#     def __init__(self):
#         host = settings['MONGODB_HOST']
#         port = settings['MONGODB_PORT']
#         dbname = settings['MONGODB_DBNAME']
#         client = pymongo.MongoClient(host=host, port=port)
#         db = client[dbname]
#         self.post = db[settings['MONGODB_COLLECTION_FR']]
#
#     def process_item(self, item, spider):
#         data = dict(item)
#         self.post.insert(data)
#         return item
