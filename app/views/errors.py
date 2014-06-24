from flask import render_template, request, g
from .. import app
from .. import nav
from .. import templatevars


@app.errorhandler(404)
def not_found(error):
    return render_template(
        'errors/404.html',
        nav_items = nav.items(app),
        page = templatevars.parse(request)
    ), 404


@app.errorhandler(500)
def server_error(error):
    return render_template(
        'errors/500.html',
        nav_items = nav.items(app),
        page = templatevars.parse(request)
    ), 500
