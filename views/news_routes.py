# views/news_routes.py

from flask import Blueprint, render_template, request
from controllers.news_controller import fetch_top_headlines, fetch_news_by_query

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route('/')
def home():
    """Home route to display top headlines."""
    selected_country = request.args.get('country', 'us')
    category = request.args.get('category', None)

    # Fetch top headlines
    news = fetch_top_headlines(country=selected_country, category=category)

    return render_template('index.html', news=news, selected_country=selected_country)

@news_blueprint.route('/news/<query>')
def category_news(query):
    """Fetch news for a specific category."""
    news = fetch_news_by_query(query=query)
    return render_template('index.html', news=news, selected_country='us')
