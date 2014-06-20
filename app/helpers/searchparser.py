import os.path
from collections import defaultdict

from .. lib.commandline import CommandLine
from . searchtermparser import SearchTermFilter


class SearchParser:

    term_limit = 5

    def search(self, path):
        terms = self._get_terms_from_path(path)
        matches = _SearchResultsParser()._search_for_matches(terms)
        results = { 'terms': terms, 'matches': matches }
        return results

    def _get_terms_from_path(self, path):
        words = path.split('/')
        filtered = SearchTermFilter().filter(words)
        terms = filtered[:self.term_limit]
        return terms


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
        command = ['grep', '-l', '-r', '-i', term, 'docs/']
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
