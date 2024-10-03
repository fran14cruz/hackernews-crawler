"""
File name: test_scraper.py
Author: Francisco Cruz
Created: 03-10-2024
Version: 1.0
Description: Test for scraper.py
"""
import pytest
from scraper import scrape_hacker_news

# Mock requests.get to avoid real HTTP requests
@pytest.fixture
def mock_hacker_news(mocker):
    mock_response = mocker.patch('requests.get')
    with open('./mocks/hacker_news_page.html', 'r') as f:
        mock_response.return_value.text = f.read()

def test_scraper_returns_correct_number_of_entries(mock_hacker_news):
    entries = scrape_hacker_news()
    # Assert that the length of the entries is 30
    assert len(entries) == 30

def test_scraper_entry_fields(mock_hacker_news):
    entries = scrape_hacker_news()

    # Check that the first entry has the correct fields
    first_entry = entries[0]
    assert 'number' in first_entry
    assert 'title' in first_entry
    assert 'points' in first_entry
    assert 'comments' in first_entry

    # Check that the fields are non-empty
    assert isinstance(first_entry['number'], int)
    assert isinstance(first_entry['title'], str) and first_entry['title'] != ''
    assert isinstance(first_entry['points'], int)
    assert isinstance(first_entry['comments'], int)


def test_scraper_handles_missing_points_or_comments(mock_hacker_news):
    entries = scrape_hacker_news()

    entry_with_missing_data = {}
    # Find and entry with zero comments or points
    for entry in entries:
        if entry['points'] == 0 or entry['comments'] == 0:
            entry_with_missing_data = entry
            break

    # Assert that it correctly handles missing points or comments
    assert entry_with_missing_data['points'] == 0 or isinstance(entry_with_missing_data['points'], int)
    assert entry_with_missing_data['comments'] == 0 or isinstance(entry_with_missing_data['comments'], int)