from flask import render_template, request, g
from .. import app
from .. import nav
from .. import templatevars
from .. documents import document


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def page(path):
    return render_template(
        'page.html',
        content = document(path),
        nav_items = nav.items(app),
        page = templatevars.parse(request)
    )

# {{ page.body_class }}
# {{ page.page_title }}

# page = templatevars.parse(request)

# requests.py

# templatevars/__init__.py => parse()
# templatevars/bodyclass.py => BodyClass()
# templatevars/pagetitle.py => PageTitle()
