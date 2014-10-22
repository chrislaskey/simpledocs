import os
import re


def items(app):
    base_url = '/' + app.config["BASE_URL"].strip('/')
    dir = app.config["DOCUMENTS_DIR"]
    creator = NavigationCreator(base_url)
    creator.add_file_filter(ImageFiletypeFilter())
    return creator.create(dir)


class NavigationCreator:

    def __init__(self, base_url = '/'):
        self.base_url = base_url
        self.nav = []
        self.file_filters = []

    def add_file_filter(self, filter):
        self.file_filters.append(filter)

    def create(self, path):
        self.path = path
        self.nav = self._walk(path)
        return self.nav

    def _walk(self, path):
        for root, dirs, files in os.walk(path):
            url_root = self._parse_url_root(root)
            level = self._parse_level(root)
            files = self._parse_filenames(files)
            contents = {
                "root": url_root,
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

    def _parse_url_root(self, root):
        relative_root = self._parse_relative_root(root)
        url_root = self.base_url + '/' + relative_root
        return url_root.rstrip('/')

    def _parse_relative_root(self, root):
        if root.startswith(self.path):
            trim_to = len(self.path)
            root = root[trim_to:]
        return root.lstrip('/')

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
        filtered = self._file_type_filters(files)
        filename = self._parse_filename
        files = [{"name":filename(x), "path":x } for x in filtered]
        return files

    def _file_type_filters(self, files):
        for filter in self.file_filters:
            files = filter.process(files)
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


class ImageFiletypeFilter:

    disallowed = ['png', 'jpg', 'jpeg', 'gif']

    def process(self, files):
        filtered = []
        for filename in files:
            extension = self._get_extension(filename)
            if extension not in self.disallowed:
                filtered.append(filename)
        return filtered

    def _get_extension(self, filename):
        period_location = filename.find('.')
        if period_location == -1:
            return ''
        extension = filename[(period_location + 1):]
        return extension.lower()
