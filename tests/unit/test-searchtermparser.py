# -*- coding: utf8 -*-


from nose.tools import *
from app.search import terms


def process_terms(search_string):
    words = terms.parse(search_string)
    keywords = terms.verify(words)
    uri = terms.encode(keywords)
    return uri


class TestSearchTerms:

    def test_empty_string_returns_empty_list(self):
        search_string = ''
        expected = ''

        result = process_terms(search_string)
        assert_equal(result, expected)

    def test_single_word(self):
        search_string = 'aLongSearch-Word_with_allowedCharacters25'
        expected = 'aLongSearch-Word_with_allowedCharacters25'

        result = process_terms(search_string)
        assert_equal(result, expected)

    def test_multiple_words(self):
        search_string = 'includes ill.egal ../ characters'
        expected = 'includes/illegal/characters'

        result = process_terms(search_string)
        assert_equal(result, expected)

    def test_a_malicious_command(self):
        search_string = '/bin/rm -rf . ../'
        expected = 'binrm/-rf'

        result = process_terms(search_string)
        assert_equal(result, expected)

    def test_invalid_characters(self):
        search_string = 'Invalid`~!@#$%^&*()-_=+[{}]\|;:\',.<>?/Characters'
        expected = 'Invalid-_Characters'

        result = process_terms(search_string)
        assert_equal(result, expected)

    def test_query_over_word_limit(self):
        search_string = 'Search for file.txt and other words that are over'
        expected = 'Search/for/filetxt/and/other'

        result = process_terms(search_string)
        assert_equal(result, expected)
