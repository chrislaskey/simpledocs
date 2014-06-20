import codecs
import os.path


class ContentLoader:

    def load(self, file_path):
        return self._read_file(file_path)

    def _read_file(self, file_path):
        if not os.path.isfile(file_path):
            return u'';
        input_file = codecs.open(file_path, mode="r", encoding="utf-8")
        unicode_text = input_file.read()
        return unicode_text
