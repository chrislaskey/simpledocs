virtualenv_site_packages = [
    '/usr/lib/virtualenvs/simpledocs/lib/python2.6/site-packages/',
    '/usr/lib/virtualenvs/simpledocs/lib/python2.7/site-packages/'
]

import os, sys
sys.path.insert(0, os.path.dirname(__file__))

for package_path in virtualenv_site_packages:
    if os.path.isdir(package_path):
        sys.path.insert(0, package_path)

from app import app as application

if not application.debug:
    import logging
    this_dir = os.path.dirname(__file__)
    log_file = os.path.join(this_dir, 'app/production.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    application.logger.addHandler(file_handler)
