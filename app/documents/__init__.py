from . import html
from . import unicode


def document(path):
    as_unicode = unicode.file(path)
    as_html = html.from_markdown(as_unicode)
    return as_html
