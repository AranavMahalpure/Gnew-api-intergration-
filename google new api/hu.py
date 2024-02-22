from flask import Flask, jsonify,render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual GNews API key
API_KEY = 'ea1b3162ceb2afb80e14a64088bb25e0'
BASE_URL = 'https://gnews.io/api/v4/search'
def energy_news():
    # Parameters for the GNews API request
    params = {
        'q': 'energy',
        'token': API_KEY,
        'lang': 'en',
        'country': 'us'  # You can adjust the country if needed
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # Filter news articles related to energy
        energy_articles = [article for article in data['articles'] if 'energy' in article['title'].lower()]
        return jsonify(energy_articles)
    else:
        return jsonify({'error': 'Failed to fetch news'}), 500
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
