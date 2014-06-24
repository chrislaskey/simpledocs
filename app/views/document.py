from flask import render_template, g
from .. documents import document
from .. import search
from .. import app

from .. helpers.pageprocessing import common_page_processing


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    common_page_processing()
    g.templatevars['content'] = document(path)
    g.templatevars['nav_items'] = nav.items(app)
    return render_template('page.html', **g.templatevars)
