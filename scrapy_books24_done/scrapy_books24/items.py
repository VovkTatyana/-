# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBooks24Item(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_discounted = scrapy.Field()
    author = scrapy.Field()
    genre = scrapy.Field()
    release_year = scrapy.Field()
    publisher = scrapy.Field()
    rating = scrapy.Field() 
    link = scrapy.Field()
    number_of_reviews = scrapy.Field()
    _id = scrapy.Field()
