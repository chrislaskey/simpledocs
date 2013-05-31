import os

class NavigationCreator:

    def __init__(self):
        self.nav = []

    def create(self, path):
        self.nav = self._walk(path)
        return self.nav

    def _walk(self, path):
        for root, dirs, files in os.walk(path):
            join = os.path.join
            files = [join(root, x) for x in files]

            if dirs:
                dir_files = []
                for dir in dirs:
                    fulldir = os.path.join(root, dir)
                    dir_files = dir_files + self._walk(fulldir)
                return files + dir_files
            else:
                return files
