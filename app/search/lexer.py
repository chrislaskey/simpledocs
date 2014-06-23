import re
from .. import app


word_limit = app.config["SEARCH_TERM_WORD_LIMIT"]


def tokenize(search_string):
    words = _parse_words(search_string)
    filtered_words = _filter_characters(words)
    terms = filtered_words[:word_limit]
    return terms


def _parse_words(search_string):
    split_limit = word_limit + 3
    words = search_string.split(' ', split_limit)
    return words


def _filter_characters(words):
    filter = app.config["SEARCH_TERM_CHARACTER_FILTER"]
    filtered = [ re.sub(filter, '', x) for x in words if x]
    return filtered
