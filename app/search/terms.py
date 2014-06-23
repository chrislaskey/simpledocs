import re
from .. import app


limit = app.config["SEARCH_TERM_WORD_LIMIT"]


def parse(string):
    split_limit = limit + 3
    words = search_string.split(' ', split_limit)
    return words


def verify(words):
    filter = app.config["SEARCH_TERM_CHARACTER_FILTER"]
    filtered = [ re.sub(filter, '', x) for x in words if x]
    terms = filtered[:limit]
    return terms


def encode(terms):
    uri = '/'.join(terms)
    return uri


def decode(uri):
    terms = uri.split('/')
    return terms
