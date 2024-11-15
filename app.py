# app.py

from flask import Flask
from views.news_routes import news_blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(news_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
