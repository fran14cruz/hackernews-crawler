# Import statements
import re


# Filter entries with more than five words in the title ordered by the number of comments first
# otherwise filter entries ordered by points
def filter_by_word_count(entries, more_than_five):
    """
    :param entries: dictionary with retrieved articles
    :param more_than_five: True or False
    :return: sorted list of entries
    """
    word_split_regex = r"\b[\w'-]+\b"

    # Helper function to count words in the title after cleaning up standalone underscores
    def word_count(title):
        cleaned_title = title.replace(" _ ", " ")
        return len(re.findall(word_split_regex, cleaned_title))

    # Filter entries based on length condition using list comprehension
    filtered_entries = [
        entry for entry in entries
        if (word_count(entry['title']) > 5 if more_than_five else word_count(entry['title']) <= 5)
    ]

    # Sort entries by comments or points using sorted function and key parameter
    sort_key = 'comments' if more_than_five else 'points'
    return sorted(filtered_entries, key=lambda x: x[sort_key], reverse=False)  # ascending order