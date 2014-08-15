import os.path
from .. import app


def url_to_path(url):
    base_url = '/' + app.config['BASE_URL'].strip('/')
    dir = app.config['DOCUMENTS_DIR'].rstrip('/')

    if url.startswith(base_url):
        trim_to = len(base_url)
        url = url[trim_to:]

    file_path = url.lstrip('/')

    return dir + '/' + file_path

def readme():
    readme = app.config['README_FILE']
    here = os.path.dirname(__file__)
    path = os.path.join(here, readme)
    abspath = os.path.abspath(path)
    return abspath
