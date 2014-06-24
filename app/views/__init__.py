from flask import request, redirect, url_for, render_template, g
from .. import nav
from .. import app

from .. helpers.pageprocessing import common_page_processing

from . import document
from . import search


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
