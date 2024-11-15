import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines'
NEWS_API_EVERYTHING_URL = 'https://newsapi.org/v2/everything'


def fetch_top_headlines(country='us', category=None):
    """Fetch top headlines based on country and category."""
    params = {
        'apiKey': NEWS_API_KEY,
        'country': country,
        'category': category
    }
    response = requests.get(NEWS_API_BASE_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [
            article for article in articles
            if article.get('title') and article.get('description') and article.get('urlToImage')
        ]
    else:
        print(f"Error fetching news: {response.status_code}")
        return []


def fetch_news_by_query(query='India', from_date='2024-11-10', sort_by='popularity'):
    """Fetch news based on a query term."""
    params = {
        'apiKey': NEWS_API_KEY,
        'q': query,
        'from': from_date,
        'sortBy': sort_by
    }
    response = requests.get(NEWS_API_EVERYTHING_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [
            article for article in articles
            if article.get('title') and article.get('description') and article.get('urlToImage')
        ]
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
