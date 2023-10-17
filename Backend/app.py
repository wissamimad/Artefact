import os
from flask import Flask, Response, request, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.json_util import dumps
import urllib.parse

load_dotenv()

app = Flask(__name__)

# Get the username and password from the .env file
mongo_db_username = os.environ.get("db_username")
mongo_db_password = os.environ.get("db_password")

# Encode the username and password
encoded_username = urllib.parse.quote_plus(mongo_db_username)
encoded_password = urllib.parse.quote_plus(mongo_db_password)

# construct the MongoDB connection string
mongo_db_url = f'mongodb+srv://{encoded_username}:{encoded_password}@cluster0.kb6g8wm.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(mongo_db_url)
db = client['Artefact']
collection = db['bbc_news']

# Search for all articles or for a specific keyword in the content
@app.get("/api/article_by_content")
def get_articles_by_content():
    keywords = request.args.get('keywords')
    filter = {} if keywords is None else {"body": {"$regex": keywords, "$options": "i"}}
    articles = list(collection.find(filter))

    response = Response(
        response=dumps(articles), status=200,  mimetype="application/json")
    return response

# Search for all articles or for a specific keyword in the headline
@app.get("/api/article_by_headline")
def get_articles_by_headline():
    keywords = request.args.get('keywords')
    filter = {} if keywords is None else {"headline": {"$regex": keywords, "$options": "i"}}
    articles = list(collection.find(filter))

    response = Response(
        response=dumps(articles), status=200,  mimetype="application/json")
    return response