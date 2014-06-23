from .. helpers.searchparser import SearchParser
from . query import search_query
from . import terms


def terms(request):
    search_string = request.form.get('search', '')
    words = terms.parse(search_string)
    terms = terms.verify(words)
    uri = terms.encode(terms)
    return uri


def results(uri):
    words = terms.decode(uri)
    terms = terms.verify(words)
    results = search_query(terms)
    return results
