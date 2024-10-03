from flask import Flask, render_template
from scraper import scrape_hacker_news
from filters import filter_by_word_count

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape') # route to retrieve entries
def scrape():
    entries = scrape_hacker_news()
    return render_template('scrape.html', entries=entries)

@app.route('/filter/more_than_five_words') # route to filter entries
def filter_more_than_five_words():
    entries = scrape_hacker_news()
    filtered_entries = filter_by_word_count(entries, True)
    return render_template('filtered.html', entries=filtered_entries, filter_type="More than 5 words")

@app.route('/filter/five_or_less_words') # route to filter entries
def filter_five_or_less_words():
    entries = scrape_hacker_news()
    filtered_entries = filter_by_word_count(entries, False)
    return render_template('filtered.html', entries=filtered_entries, filter_type="5 or fewer words")

if __name__ == '__main__':
    app.run()
