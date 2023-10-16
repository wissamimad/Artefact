import scrapy

class ArticleItems(scrapy.Item):
    """Scrapy Item class that represents the news article we want to parse."""

    body = scrapy.Field()
    author = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()