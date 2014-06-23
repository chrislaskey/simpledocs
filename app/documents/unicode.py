import codecs
import os.path
from . import paths


def file(path):
    unicode_text = None
    loader = _return_file_contents_as_unicode
    if path:
        unicode_text = loader(path)
    if not unicode_text:
        unicode_text = loader(paths.readme())
    if not unicode_text:
        unicode_text = app.config["DEFAULT_TEXT"]
    return unicode_text


def _return_file_contents_as_unicode(path):
    if not os.path.isfile(path):
        return u'';
    input_file = codecs.open(path, mode="r", encoding="utf-8")
    unicode_text = input_file.read()
    return unicode_text
