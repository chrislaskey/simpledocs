from flask import request, redirect, url_for, render_template, g
from .. documents import document
from .. import search
from .. import nav
from .. import app

from .. helpers.pageprocessing import common_page_processing


@app.route('/parse-search', methods = ['post'])
def parse_search():
    redirect_to = url_for('search_page', terms=search.parse(request))
    return redirect(redirect_to)


@app.route('/search/', defaults={'terms': ''})
@app.route('/search/<path:terms>')
def search_page(terms):
    common_page_processing()
    search_results = search.results(terms)
    http_code = 200 if search_results['success'] else 404
    g.templatevars['search_results'] = search_results
    g.templatevars['nav_items'] = nav.items(app)
    return render_template('site/search.html', **g.templatevars), http_code


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    common_page_processing()
    g.templatevars['content'] = document(path)
    g.templatevars['nav_items'] = nav.items(app)
    return render_template('page.html', **g.templatevars)


@app.errorhandler(404)
def not_found(error):
    common_page_processing()
    g.templatevars['nav_items'] = nav.items(app)
    return render_template('errors/404.html', **g.templatevars), 404


@app.errorhandler(500)
def server_error(error):
    common_page_processing()
    g.templatevars['nav_items'] = nav.items(app)
    return render_template('errors/500.html', **g.templatevars), 500
