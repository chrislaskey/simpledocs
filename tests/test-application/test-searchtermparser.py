# -*- coding: utf8 -*-

from nose.tools import *
from application.searchparser import _SearchTermParser

class TestSearchTermParser:

    def setup(self):
        "Set up test fixtures"
        self.stp = _SearchTermParser()

    def teardown(self):
        "Tear down test fixtures"

    def test_empty_string_returns_empty_list(self):
        search_string = ''
        expected = ['']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)

    def test_single_word(self):
        search_string = 'aLongSearch-Word_with_allowedCharacters25'
        expected = ['aLongSearch-Word_with_allowedCharacters25']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)

    def test_word_filter_with_invalid_characters(self):
        search_string = 'Invalid`~!@#$%^&*()-_=+[{}]\|;:\',.<>?/Characters'
        expected = ['Invalid-_Characters']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)

    def test_simple_query(self):
        search_string = 'Search for term'
        expected = ['Search', 'for', 'term']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)

    def test_query_with_invalid_characters(self):
        search_string = 'Search for file.txt'
        expected = ['Search', 'for', 'filetxt']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)

    def test_query_over_word_limit(self):
        search_string = 'Search for file.txt and other words that are over'
        expected = ['Search', 'for', 'filetxt', 'and', 'other']

        result = self.stp.parse(search_string)
        assert_equal(result, expected)
