#!/usr/bin/env python

import os
import sys
this_dir = os.path.dirname(__file__)
sys.path.insert(0, this_dir)

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path()

from main import app as application

if not application.debug:
    import logging
    this_dir = os.path.dirname(__file__)
    log_file = os.path.join(this_dir, 'production.log')
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.WARNING)
    application.logger.addHandler(file_handler)

application.jinja_env.line_statement_prefix = '%'
