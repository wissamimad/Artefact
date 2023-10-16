import scrapy
from bbc_articles.items import ArticleItems

class bbcSpider(scrapy.Spider):
    name = "bbc-spider"
    start_urls = ['https://www.bbc.com/news']

    def parse(self, response):
        # Testing the parse's result for min and max requests
        """
        @url http://www.bbc.com/news
        @returns requests 40 50
        """
        article_selector = "a.gs-c-promo-heading[href^='/news']"

        yield from response.follow_all(
            response.css(article_selector), self.parse_article
        )
        
    def parse_article(self, response):
        # Testing the parse_article's result for 1 article
        """
        @url https://www.bbc.com/news/world-middle-east-67105618
        @returns items 1
        @scrapes body author headline url
        """
        # Retrieving the necessary data for each part
        body_selector = 'div[data-component="text-block"] ::text'
        author_selector = 'div.ssrcss-68pt20-Text-TextContributorName::text'
        headline_selector = '#main-heading::text'


        body = response.css(body_selector).getall()
        author = response.css(author_selector).get()
        headline = response.css(headline_selector).get()
        url = response.url
        
        # The body needs to contain a text-block,otherwise it's not needed
        if body:
            if author:
                # Removing unnecessary characters
                author = author.replace("By ", "")

            # Creating an item from the retrieved information for further processing
            item = ArticleItems(body=body, author=author, headline=headline, url=url)

            yield item