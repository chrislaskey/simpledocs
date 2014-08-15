from . import html
from . import unicode
from . paths import url_to_path


def document(url):
    as_path = url_to_path(url)
    as_unicode = unicode.file(as_path)
    as_html = html.from_markdown(as_unicode)
    return as_html
