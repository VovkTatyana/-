# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient 




class ScrapyBooks24Pipeline:

    def __init__(self):
        clieent_TV = MongoClient('localhost:27017')
        self.db = clieent_TV.books24

        
    def process_item(self, item, spider):
        collections_books24 = self.db[spider.name]

        collections_books24.insert_one(item)

        return item
