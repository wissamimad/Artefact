# Scrapy settings for Artefact project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = "Artefact"

SPIDER_MODULES = ["bbc_articles.spiders"]
NEWSPIDER_MODULE = "bbc_articles.spiders"

# Get the username and password from the .env file
mongo_db_username = os.environ.get("db_username")
mongo_db_password = os.environ.get("db_password")

# Encode the username and password
encoded_username = urllib.parse.quote_plus(mongo_db_username)
encoded_password = urllib.parse.quote_plus(mongo_db_password)

MONGO_URI = f'mongodb+srv://{encoded_username}:{encoded_password}@cluster0.kb6g8wm.mongodb.net/?retryWrites=true&w=majority&ssl=true'
MONGO_DATABASE = "Artefact"
MONGODB_COLLECTION = "bbc_news"
# Enable the MongoDB pipeline
ITEM_PIPELINES = {
    'bbc_articles.pipelines.MongoPipeline': 300,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
