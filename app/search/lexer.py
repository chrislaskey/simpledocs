import re
from .. import app


def tokenize(request):
    return SearchTermParser().get_as_uri(request)


class SearchTermParser:

    ''' Parses raw search strings into filtered search terms '''

    word_limit = app.config["SEARCH_TERM_WORD_LIMIT"]

    def get_as_uri(self, request):
        search_string = request.form.get('search', '')
        terms = self.parse(search_string)
        uri = '/'.join(terms)
        return uri

    def parse(self, search_string):
        words = self._split_into_words(search_string)
        all_terms = SearchTermFilter().filter(words)
        terms = all_terms[:self.word_limit]
        return terms

    def _split_into_words(self, search_string):
        split_limit = self.word_limit + 1
        words = search_string.split(' ', split_limit)
        return words


class SearchTermFilter:

    def filter(self, terms):
        filter = app.config["SEARCH_TERM_CHARACTER_FILTER"]
        filtered = [ re.sub(filter, '', x) for x in terms if x]
        return filtered
