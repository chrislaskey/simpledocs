import os.path
from .. import app


def readme():
    readme = app.config['README_FILE']
    here = os.path.dirname(__file__)
    path = os.path.join(here, readme)
    abspath = os.path.abspath(path)
    return abspath
