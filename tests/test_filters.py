"""
File name: test_filters.py
Author: Francisco Cruz
Created: 03-10-2024
Version: 1.0
Description: Test for filters.py
"""
from filters import filter_by_word_count

# Sample data
entries = [
    {'number': 1, 'title': 'This title has 5 words', 'points': 100, 'comments': 50},
    {'number': 2, 'title': 'This is a longer title with more words', 'points': 400, 'comments': 30},
    {'number': 3, 'title': 'Expect a reduction of 40% which is $50', 'points': 0, 'comments': 7},
    {'number': 4, 'title': 'This is - a self-explained example', 'points': 300, 'comments': 100},
    {'number': 5, 'title': 'Is this a long title?', 'points': 10, 'comments': 0},
]

def test_filter_more_than_five_words():
    filtered_entries = filter_by_word_count(entries, True)

    # Check that only entries with more than 5 words were included, sorted by comments
    assert len(filtered_entries) == 2  # Only two entries have more than 5 words
    assert filtered_entries[0]['comments'] <= filtered_entries[1]['comments']  # Check that they are ordered by comments

def test_filter_five_or_less_words():
    filtered_entries = filter_by_word_count(entries, False)

    # Check that only entries with 5 or fewer words were included, sorted by points
    assert len(filtered_entries) == 3  # Three entries have 5 or fewer words
    assert filtered_entries[0]['points'] <= filtered_entries[1]['points']  # Check that they are ordered by points

def test_filter_handles_titles_with_symbols():
    filtered_entries = filter_by_word_count([entries[3]], False)

    # Check that symbols don't affect word count
    assert len(filtered_entries) == 1 # it should pass the 5 or less filter
    assert filtered_entries[0]['title'] == 'This is - a self-explained example'