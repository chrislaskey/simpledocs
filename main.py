#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path(__file__)

from flask import Flask, abort, request, redirect, url_for, render_template, g
from lib.commandline import CommandLine
from lib.contentloader import ContentLoader
from lib.markdownparser import MarkdownParser
from application.pageprocessing import common_page_processing
from application.searchparser import SearchParser

app = Flask(__name__)

@app.route('/parse-search-terms', methods = ['post'])
def parse_search_terms(terms):
    pass
    # search_terms = searchter
    # search_results = searchparser().search(request)
    # g.templatevars['search_results'] = search_results
    # return render_template('site/search.html', **g.templatevars)

@app.route('/search', defaults={'terms': ''})
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

if __name__ == '__main__':
    app.debug = True
    app.run()
