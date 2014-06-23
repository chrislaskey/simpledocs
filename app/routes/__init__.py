from flask import request, redirect, url_for, render_template, g
from .. documents import document
from .. helpers.pageprocessing import common_page_processing
from .. helpers.searchparser import SearchParser
from .. helpers.searchtermparser import SearchTermParser
# from .. nav import navigation
# from .. search import search_terms, search_results
from .. import app


@app.route('/parse-search-terms', methods = ['post'])
def parse_search_terms():
    search_term_uri = SearchTermParser().get_as_uri(request)
    redirect_to = url_for('search', terms=search_term_uri)
    return redirect(redirect_to)


@app.route('/search/', defaults={'terms': ''})
@app.route('/search/<path:terms>')
def search(terms):
    common_page_processing()
    search_parser = SearchParser()
    search_results = search_parser.search(terms)
    http_code = 200 if search_parser.is_successful(search_results) else 404
    g.templatevars['search_results'] = search_results
    return render_template('site/search.html', **g.templatevars), http_code


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    common_page_processing()
    g.templatevars['content'] = document(path)
    return render_template('page.html', **g.templatevars)


@app.errorhandler(404)
def not_found(error):
    common_page_processing()
    return render_template('errors/404.html', **g.templatevars), 404


@app.errorhandler(500)
def server_error(error):
    common_page_processing()
    return render_template('errors/500.html', **g.templatevars), 500
