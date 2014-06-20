from flask import abort, request, redirect, url_for, render_template, g
from .. lib.contentloader import ContentLoader
from .. lib.markdownparser import MarkdownParser
from .. helpers.pageprocessing import common_page_processing
from .. helpers.searchparser import SearchParser
from .. helpers.searchtermparser import SearchTermParser

# from .. import app
# from . search import search, parse_search_terms
# from . page import page
# from . errors import not_found, server_error


@app.route('/parse-search-terms', methods = ['post'])
def parse_search_terms():
    search_term_uri = SearchTermParser().get_as_uri(request)
    redirect_to = '/search' + search_term_uri
    return redirect(redirect_to)


@app.route('/search/', defaults={'terms': ''})
@app.route('/search/<path:terms>')
def search(terms):
    common_page_processing()
    search_results = SearchParser().search(terms)
    g.templatevars['search_results'] = search_results
    return render_template('site/search.html', **g.templatevars)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    common_page_processing()

    unicode_text = ContentLoader().load(path)
    if not unicode_text:
        unicode_text = ContentLoader().load('readme.md')
    html_content = MarkdownParser().parse(unicode_text)
    g.templatevars['content'] = html_content

    return render_template('page.html', **g.templatevars)


@app.errorhandler(404)
def not_found(error):
    common_page_processing()
    return render_template('errors/404.html', **g.templatevars), 404


@app.errorhandler(500)
def server_error(error):
    common_page_processing()
    return render_template('errors/500.html', **g.templatevars), 500
