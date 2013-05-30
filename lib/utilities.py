import codecs
import os.path

def read_file(file_path):
    if not os.path.isfile(file_path):
        return u'';
    input_file = codecs.open(file_path, mode="r", encoding="utf-8")
    unicode_text = input_file.read()
    return unicode_text
