from flask import Flask, jsonify, Response
from scrape import scrape_news_articles, scrape_news_archives
import json

app = Flask(__name__)

# CORS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Main Index
@app.route('/', methods=['GET'])
def get_home():
    return jsonify({
            'author': 'Sandip Bhagat',
            'author_url': 'http://sandipbgt.com',
            'base_url': 'https://indian-embassy-news.herokuapp.com',
            'api_url': 'https://indian-embassy-news.herokuapp.com/api',
            'project_name': 'indian-embassy-news',
            'project_demo': 'http://sandipbgt.com/indian-embassy-news',
            'project_url': 'https://github.com/sandipbgt/indian-embassy-news',
        })

# API Index
@app.route('/api', methods=['GET'])
def get_api_home():
    return jsonify({
            'articles': 'https://indian-embassy-news.herokuapp.com/api/articles',
            'archives': 'https://indian-embassy-news.herokuapp.com/api/archives',
        })

# Articles API
@app.route('/api/articles', methods=['GET'])
def get_articles():
    return Response(json.dumps({'articles': scrape_news_articles()}), mimetype='application/json')

# Archives API
@app.route('/api/archives', methods=['GET'])
def get_archives():
    return Response(json.dumps({'archives': scrape_news_archives()}), mimetype='application/json')


if __name__ == '__main__':
    app.run()