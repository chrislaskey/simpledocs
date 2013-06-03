#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path(__file__)

from flask import Flask, abort, request, redirect, url_for, render_template, g
from lib.commandline import CommandLine
from lib.markdownparser import MarkdownParser
from lib.navigationcreator import NavigationCreator
from lib.searchparser import SearchParser
from lib.utilities import read_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    base_path = "docs"
    test_file_path = "readme.md"
    unicode_text = read_file(test_file_path)
    html_content = MarkdownParser().parse(unicode_text)
    nav_items = NavigationCreator().create(base_path)
    templatevars = {
        "content": html_content,
        "nav_items": nav_items
    }
    return render_template('page.html', **templatevars)

@app.route('/search', methods = ['GET', 'POST'])
def search():
    base_path = "docs"
    # test_file_path = "readme.md"
    # unicode_text = read_file(test_file_path)
    # html_content = MarkdownParser().parse(unicode_text)

    if request.method == 'POST':
        search_value = request.form.get('search', '')
    nav_items = NavigationCreator().create(base_path)
    templatevars = {
        "content": search_value,
        "nav_items": nav_items
    }
    return render_template('site/search.html', **templatevars)

if __name__ == '__main__':
    app.debug = True
    app.run()
