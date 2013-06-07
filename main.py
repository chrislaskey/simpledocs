#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path(__file__)

from flask import Flask, abort, request, redirect, url_for, render_template, g
from lib.commandline import CommandLine
from lib.markdownparser import MarkdownParser
from lib.searchparser import SearchParser
from lib.utilities import read_file
from application.pageprocessing import common_page_processing

app = Flask(__name__)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    common_page_processing()

    search_value = 'No search value found'
    if request.method == 'POST':
        search_value = request.form.get('search', '')
    g.templatevars['content'] = search_value

    return render_template('site/search.html', **g.templatevars)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    common_page_processing()

    test_file_path = 'readme.md'
    unicode_text = read_file(test_file_path)
    html_content = MarkdownParser().parse(unicode_text)
    g.templatevars['content'] = html_content

    return render_template('page.html', **g.templatevars)

if __name__ == '__main__':
    app.debug = True
    app.run()
