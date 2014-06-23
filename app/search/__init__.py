from .. helpers.searchparser import SearchParser
from . lexer import tokenize


def terms(request):
    terms = tokenize(request)
    return terms

def results(terms):
    search_parser = SearchParser()
    results = search_parser.search(terms)
    results['has_results'] = search_parser.is_successful(results)
    return results
