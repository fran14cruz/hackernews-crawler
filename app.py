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

@app.route('/filter/more_than_five_words') # route to filter entries
def filter_more_than_five_words():
    entries = scrape_hacker_news()
    filtered = filter_by_word_count(entries, True)
    return jsonify(filtered)

@app.route('/filter/five_or_less_words')
def filter_five_or_less_words():
    entries = scrape_hacker_news()
    filtered = filter_by_word_count(entries, False)
    return jsonify(filtered)


if __name__ == '__main__':
    app.run(debug=True)
