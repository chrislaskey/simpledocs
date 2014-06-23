from .. helpers.searchparser import SearchParser
from . lexer import tokenize


def terms(request):
    search_string = request.form.get('search', '')
    terms = tokenize(search_string)
    as_uri = '/'.join(terms)
    return as_uri


def results(terms):
    search_parser = SearchParser()
    results = search_parser.search(terms)
    results['has_results'] = search_parser.is_successful(results)
    return results
