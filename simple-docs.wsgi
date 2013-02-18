#!/usr/bin/env python

from lib.environment import Environment
Environment().add_virtualenv_site_packages_to_path()

from main import app as application
application.jinja_env.line_statement_prefix = '%'
