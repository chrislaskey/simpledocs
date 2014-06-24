import os
import re


def items(app):
    dir = app.config["DOCUMENTS_DIR"]
    return NavigationCreator().create(dir)


class NavigationCreator:

    def __init__(self):
        self.nav = []

    def create(self, path):
        self.nav = self._walk(path)
        return self.nav

    def _walk(self, path):
        for root, dirs, files in os.walk(path):
            level = self._parse_level(root)
            files = self._parse_filenames(files)
            contents = {
                "root": root,
                "level": level,
                "files": files,
                "dirs": []
            }

            if dirs:
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    dir_files = self._walk(dir_path)
                    contents["dirs"].append(dir_files)
            return contents

    def _parse_level(self, root):
        relative = self._get_relative_root(root)
        without_prefix = self._strip_numeric_prefix(relative)
        level = self._create_title_from_slug(without_prefix)
        return level

    def _strip_numeric_prefix(self, text):
        stripped = re.sub(r'^[0-9_-]*(.*)', r'\1', text)
        return stripped

    def _get_relative_root(self, root):
        last_slash = root.rfind('/')
        if not last_slash:
            return root
        cut_from = last_slash + 1
        return root[cut_from:]

    def _create_title_from_slug(self, text):
        replaced_text = re.sub(r'[-_]+', ' ', text)
        stripped_text = replaced_text.strip()
        return stripped_text.title()

    def _parse_filenames(self, files):
        name = self._parse_filename
        files = [{"name":name(x), "path":x } for x in files]
        return files

    def _parse_filename(self, filename):
        without_extension = self._remove_extension(filename)
        without_prefix = self._strip_numeric_prefix(without_extension)
        return self._create_title_from_slug(without_prefix)

    def _remove_extension(self, filename):
        extension = filename.find('.')
        if extension != -1:
            without_extension = filename[:extension]
        else:
            without_extension = filename
        return without_extension
