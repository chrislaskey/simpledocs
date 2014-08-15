from flask import request, redirect, url_for, render_template
from .. import app
from .. import nav
from .. import search
from .. import templatevars


@app.route('/parse-search', methods = ['post'])
def parse_search():
    redirect_to = url_for('search_page', terms=search.parse(request))
    return redirect(redirect_to)


@app.route('/search/', defaults={'terms': ''})
@app.route('/search/<path:terms>')
def search_page(terms):
    search_results = search.results(terms)
    http_code = 200 if search_results['success'] else 404
    return render_template(
        'site/search.html',
        search_results = search_results,
        nav_items = nav.items(app),
        page = templatevars.parse(request)
    ), http_code
