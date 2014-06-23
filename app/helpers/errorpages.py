import os.path


def readme_path():
    here = os.path.dirname(__file__)
    readme = '../../readme.md'
    path = os.path.join(here, readme)
    return os.path.abspath(path)
