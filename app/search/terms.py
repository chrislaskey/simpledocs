import re
from .. import app


limit = app.config["SEARCH_TERM_WORD_LIMIT"]


def parse(search_string):
    split_limit = limit + 3
    words = search_string.split(' ', split_limit)
    return words


def verify(words):
    filter = app.config["SEARCH_TERM_CHARACTER_FILTER"]
    filtered = [ re.sub(filter, '', x) for x in words if x ]
    verified_terms = [ x for x in filtered if x ]
    terms = verified_terms[:limit]
    return terms


def encode(terms):
    uri = '/'.join(terms)
    return uri


def decode(uri):
    terms = uri.split('/')
    return terms
