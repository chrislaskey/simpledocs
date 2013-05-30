#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path(__file__)

from flask import Flask, abort, request, redirect, url_for, render_template, g
from lib.commandline import CommandLine
from lib.markdownparser import MarkdownParser
from lib.utilities import read_file
from lib.search import search
app = Flask(__name__)

@app.route('/')
def hello_world():
    test_file_path = "readme.md"
    unicode_text = read_file(test_file_path)
    markdown_parser = MarkdownParser()
    html_content = markdown_parser.parse(unicode_text)
    nav_items = ["one", "two", "three"]
    templatevars = {
        "content": html_content,
        "nav_items": nav_items
    }
    return render_template('page.html', **templatevars)

if __name__ == '__main__':
    app.jinja_env.line_statement_prefix = '%'
    app.debug = True
    app.run()
