from flask import Flask, render_template, jsonify
from scraper import scrape_hacker_news
from filters import filter_by_word_count

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape') # route to retrieve entries
def scrape():
    entries = scrape_hacker_news()
    return jsonify(entries)


if __name__ == '__main__':
    app.run(debug=True)
