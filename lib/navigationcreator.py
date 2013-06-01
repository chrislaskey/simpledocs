import os

class NavigationCreator:

    def __init__(self):
        self.nav = []

    def create(self, path):
        self.nav = self._walk(path)
        import pprint
        pp = pprint.PrettyPrinter()
        pp.pprint(self.nav)
        return self.nav

    def _walk(self, path):
        for root, dirs, files in os.walk(path):
            contents = {
                "root": root,
                "files": files,
                "dirs": []
            }

            if dirs:
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    dir_files = self._walk(dir_path)
                    contents["dirs"].append(dir_files)
            return contents
