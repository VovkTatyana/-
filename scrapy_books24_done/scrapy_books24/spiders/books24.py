import scrapy
import re
from scrapy_books24.items import ScrapyBooks24Item



class Books24Spider(scrapy.Spider):

    name = "books24"
    allowed_domains = ["book24.ru"]
    start_urls = ["https://book24.ru/knigi-bestsellery/"]

    def parse(self, response):
        for link in response.css('div.product-card__image-holder a::attr(href)'):
            yield response.follow(link, callback=self.products_parse)
        
        for i in range(1, 10):
            next_page = f'https://book24.ru/knigi-bestsellery/page-{i}/'
            yield response.follow(next_page, callback=self.parse)

    def products_parse(self, response):
        book_name = re.findall('(?<=: ).*',response.css('h1.product-detail-page__title::text').get())[0]
        book_price = re.findall('[0-9]+',response.css('div.product-sidebar-price.product-sidebar__price-holder span::text').get())[0]
        book_price_discounted = re.findall('[0-9]+',response.css('div.product-sidebar-price__main-price span::text').get().strip())[0]
        book_author = response.css('dd.product-characteristic__value a::attr(title)').getall()[0]
        book_genre = response.css('dd.product-characteristic__value a::attr(title)').getall()[2]
        book_release_year = response.css('dd.product-characteristic__value::text').getall()[1]
        book_publisher = response.css('dd.product-characteristic__value a::attr(title)').getall()[3]
        book_rating = response.css('span.rating-widget__main-text::text').get().split()[0]
        book_link = response.url
        book_number_of_reviews = response.css('span.product-tabs__item-cnt::text').get().split()[0]
        


        yield ScrapyBooks24Item(
            name = book_name,
            price = book_price,
            price_discounted = book_price_discounted,
            author = book_author,
            genre = book_genre,
            release_year = book_release_year,
            publisher = book_publisher,
            rating = book_rating,
            link = book_link,
            number_of_reviews = book_number_of_reviews
        )


      