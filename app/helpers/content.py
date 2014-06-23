import os.path
from .. lib.contentloader import ContentLoader
from .. lib.markdownparser import MarkdownParser


def get_page_html(path):
    unicode_text = _get_page_or_default_text(path)
    html_content = MarkdownParser().parse(unicode_text)
    return html_content


def _get_page_or_default_text(path):
    loader = ContentLoader()
    unicode_text = None
    if path:
        unicode_text = loader.load(path)
    if not unicode_text:
        unicode_text = loader.load(_readme_path())
    if not unicode_text:
        unicode_text = _default_text()
    return unicode_text


def _default_text():
    return u"#Welcome to Simple Docs\nThis is the default page. Please refer to \
            the documentation on how to setup your documentation path."


def _readme_path():
    here = os.path.dirname(__file__)
    readme = '../../readme.md'
    path = os.path.join(here, readme)
    return os.path.abspath(path)
