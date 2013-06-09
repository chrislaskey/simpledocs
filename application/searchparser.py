import re
import os.path
from collections import defaultdict
from lib.commandline import CommandLine


class SearchParser:

    def search(self, request):
        search_string = request.form.get('search', '')
        terms = _SearchTermParser().parse(search_string)
        matches = _SearchResultsParser()._search_for_matches(terms)
        results = { 'terms': terms, 'matches': matches }
        print(results)
        return results

class _SearchTermParser:

    ''' Parses raw search strings into filtered search terms '''

    word_limit = 5

    def parse(self, search_string):
        words = self._split_into_words(search_string)
        all_terms = self._filter_words(words)
        terms = all_terms[:self.word_limit]
        return terms

    def _split_into_words(self, search_string):
        split_limit = self.word_limit + 1
        words = search_string.split(' ', split_limit)
        return words

    def _filter_words(self, words):
       filtered = [ re.sub('[^a-zA-Z0-9-_]*', '', x) for x in words]
       return filtered


class _SearchResultsParser:

    ''' Executes native file system search using Python subprocesses '''

    def _search_for_matches(self, terms):
        self.cli = CommandLine()
        self.results = defaultdict(int)
        for term in terms:
            self._search_file_names(term)
            self._search_file_contents(term)
        results_as_list = self._get_results_as_list()
        return results_as_list

    def _search_file_names(self, term):
        term = '*{0}*'.format(term)
        command = ['find', 'docs/', '-iname', term]
        options = {'raise_exception_on_failure': False}
        results = self.cli.execute(command, **options)
        self._compile_command_results(results, 3)

    def _search_file_contents(self, term):
        command = ['grep', '-l', '-r', term, 'docs/']
        options = {'raise_exception_on_failure': False}
        results = self.cli.execute(command, **options)
        self._compile_command_results(results)

    def _compile_command_results(self, results, weight=1):
        files = results.split('\n')
        filtered = [x for x in files if x]
        for file in filtered:
            file = os.path.normpath(file)
            # Using a defaultdict datatype to skip key/val instantiation
            self.results[file] += weight

    def _get_results_as_list(self):
        results_list = sorted(self.results, key=self.results.get, reverse=True)
        return results_list
