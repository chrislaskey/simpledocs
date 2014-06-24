from flask import render_template, g
from .. documents import document
from .. import nav
from .. import app

from .. helpers.pageprocessing import common_page_processing


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    common_page_processing()
    print(g.templatevars)
    return render_template(
        'page.html',
        content = document(path),
        nav_items = nav.items(app),
        # request = request.vars(request)
        **g.templatevars
    )
