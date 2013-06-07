import os

class NavigationCreator:

    def __init__(self):
        self.nav = []

    def create(self, path):
        self.nav = self._walk(path)
        return self.nav

    def _walk(self, path):
        for root, dirs, files in os.walk(path):
            level = self._get_relative_root(root)
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

    def _get_relative_root(self, root):
        last_slash = root.rfind('/')
        if not last_slash:
            return root
        cut_from = last_slash + 1
        return root[cut_from:]
