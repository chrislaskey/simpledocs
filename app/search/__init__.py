from .. helpers.searchparser import SearchParser
from .. helpers.searchtermparser import SearchTermParser


def terms(request):
    return SearchTermParser().get_as_uri(request)

def results(terms):
    search_parser = SearchParser()
    results = search_parser.search(terms)
    results['has_results'] = search_parser.is_successful(results)
    return results
