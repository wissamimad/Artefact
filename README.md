# Artefact
This is a technical assessment done for Atefact.
The code is designed to crawl a news website (http://www.bbc.com/news). Then the code inserts the scraped data into MongoDB and then it's accessible by API.

## Installation
Python is expected to be installed on your machine. 
Change directory to the top level of the project and run:

```bash
pip install -r requirements.txt
```

## Configuration

Create a  ```.env ``` file and fill in the below:
- `db_username` : The username to access the MongoDB.
- `db_password` : The password to access the MongoDB.

Then save the file in "bbc_articles" directory and "Backend" directory.

## Usage

### crawlers

Run the `bbc-spider` spider that will scrap the article from the website.

```bash
# crawl the main /news section
scrapy crawl bbc-spider
```

### Backend

Navigate to the Backend Directory:

```bash
cd Backend
```

Run the the Flask app:

```bash
flask run
```

After the app is running, call the endpoints:
```bash
# Get all articles from the database
curl http://localhost:5000/api/article_by_headline
or
curl http://localhost:5000/api/article_by_content

# Get articles by headline keywords:
curl http://localhost:5000/api/article_by_headline?keywords=<VALUE>

# Get articles by content keywords:
curl http://localhost:5000/api/article_by_content?keywords=<VALUE>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
