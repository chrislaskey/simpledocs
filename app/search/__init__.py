from .. helpers.searchparser import SearchParser
from . query import search_query
from . import terms


def parse(request):
    search_string = request.form.get('search', '')
    words = terms.parse(search_string)
    keywords = terms.verify(words)
    uri = terms.encode(keywords)
    return uri


def results(uri):
    words = terms.decode(uri)
    keywords = terms.verify(words)
    results = search_query(keywords)
    return results
