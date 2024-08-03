import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Replace with your News API key
NEWS_API_KEY = 'd154c1a3c89d4c888587d9639654f3ec' 
CATEGORIES = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

def fetch_news_by_category(category):
    url =  f'https://newsapi.org/v2/top-headlines'
    params = {
        'category': category,
        'apiKey': NEWS_API_KEY,
        'pageSize': 10  # Adjust based on the number of articles you want
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return [article['title'] for article in data.get('articles', [])]
    else:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    if not data or 'News Category' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    category = data['News Category']
    recommendations = fetch_news_by_category(category)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
