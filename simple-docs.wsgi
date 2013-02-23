#!/usr/bin/env python

import os
import sys
this_dir = os.path.dirname(__file__)
sys.path.insert(0, this_dir)

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path()

from main import app as application
application.jinja_env.line_statement_prefix = '%'
