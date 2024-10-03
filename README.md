# Hacker News Web Crawler
This is a Web Crawler application created with Flask

## Overview
This project is built with Python3 and uses the BeautifulSoup library to pull data of the first 30 entries from [Hacker News](https://news.ycombinator.com/). 

The main functionality includes:
- Scraping the first 30 entries, extracting the number, title, points, and comments for each entry.
- Filters:
  - Titles with more than 5 words are ordered by the number of comments.
  - Titles with 5 or fewer words are ordered by points.
- Automated Testing: pytest library and a mock request is used for testing.

## Technologies Used
- Python3: Main programming language.
- BeautifulSoup: For HTML parsing and web scraping.
- Flask: Framework to expose functionality through a web interface.
- pytest: For writing and running tests.
- unittest.mock: For mocking the HTTP requests during tests.

## Features
- Extracts the top 30 stories from Hacker News.
- Filters and orders the stories based on the following criteria:
  - Titles with more than 5 words, ordered by the number of comments (ascending order).
  - Titles with 5 or fewer words, ordered by points (ascending order).
- Handles cases where titles include symbols, only counting spaced words.
- Automated tests.
- Web interface for interacting with the filtering options.

## How to Run the Application
### Prerequisites
Make sure you have Python 3.x installed on your machine.

### Running the Web Crawler
1. Clone the repository into your local machine and go the project folder, i.e. ```cd hackernews-crawler```
2. Once on the project folder, install the required dependencies by running:
```
pip install -r requirements.txt
```
Note: I recommend using a virtual environment so that versions of packages keep isolated for this project.
See the notes below for instructions on how to set up a virtual environment.

3. Run the Flask app:
```
python app.py
```
4. Access the web interface at http://localhost:5000/. 
Here you can view and interact with the filtering functionality.
5. The routes used for this application are:
   - '/' renders a simple html template
   - '/scrape' rendered html displaying the 30 first entries pulled from Hacker News
   - '/filter/more_than_five_words' rendered html displaying filtered entries with titles longer than 5 words, ordered by number of comments
   - '/filter/five_or_less_words' rendered html displaying filtered entries with titles with 5 or fewer words, ordered by points
6. The project is hosted here https://hackernews-crawler.onrender.com/

## Running the Tests
The project includes automated tests using pytest.
The tests use a mock HTML file saved in tests/mocks/hacker_news_page.html
to reduce the impact of requests to the Hacker News website.
1. Run the tests by using:
```
pytest
```
This will run all tests in the tests/ directory and report the results.

## License
This project is licensed under the MIT License.

## Set Up a Virtual Environment
1. Go to the project folder with:
```
cd hackernews-crawler
```
2. Create a virtual environment by running:
```
python3 -m venv venv
```
3. Activate the virtual environment:
```
. venv/bin/activate
```
For Windows, do:
```
venv\Scripts\activate
```
4. Now you can install the dependencies of requirements.txt