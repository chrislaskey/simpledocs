#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path(__file__)

from flask import Flask, abort, request, redirect, url_for, render_template, g
from markdown import markdown
from lib.commandline import CommandLine
import codecs
app = Flask(__name__)

class MarkdownParser:

    def __init__(self, custom_options=None):
        self.options = self._get_default_options()
        if custom_options:
            self.options = self.options.update(custom_options)

    def _get_default_options(self):
        options = {
            "output_format": "html5",
            "safe_mode": "escape"
        }
        return options

    def parse(self, unicode_text):
        parsed_html = markdown(unicode_text, **self.options)
        return parsed_html

class FileReader:

    def read(self, file_path):
        input_file = codecs.open(file_path, mode="r", encoding="utf-8")
        unicode_text = input_file.read()
        return unicode_text

@app.route('/')
def hello_world():
    test_file_path = "readme.md"
    unicode_text = FileReader().read(test_file_path)
    markdown_parser = MarkdownParser()
    html_content = markdown_parser.parse(unicode_text)
    nav_items = ["one", "two", "three"]
    templatevars = {
        "content": html_content,
        "nav_items": nav_items
    }


    # TODO temporary

    # Break search into individual words.
    #   For each word:
    #       Validate query.
    #       Search for file names.
    #       Search within files.
    #       Add to list of returned pages

#     def is_valid_query(query):
#         if not query or '..' in query or query.startswith('/'):
#             return False
#         return True

#     search = '../'
#     if not is_valid_query(search):
#         return []

#     cli = CommandLine()
#     command = cli.execute_queue([
#         ['ls', '-a'],
#         ['grep', '.py']
#     ])
#     templatevars = {
#         "content": command
#     }

    return render_template('page.html', **templatevars)

if __name__ == '__main__':
    app.jinja_env.line_statement_prefix = '%'
    app.debug = True
    app.run()
