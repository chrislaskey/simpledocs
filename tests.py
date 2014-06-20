#!/usr/lib/virtualenvs/simpledocs/bin/python

# Version 0.1.1
# Updated 2014.02.01

## About
#
# Uses system wide nosetests binary to run tests. Automatically adds
# virtualenv's site-packages.
#
# Run everything it would be done from the command line. For example turn:
#     nosetests --with-coverage --cover-package=<package> --nocapture ./tests
#
# Into:
#     ./tests.py --with-coverage --cover-package=<package> --nocapture ./tests

## Requirements
#
# pip install nosetests coverage
 
## Extending this file
#
# As command line arguments pass through to nosetests, there should be no need
# to extend or change this file. Do not add os.environ[] style settings to this
# page as it will conflict with command line arguments. Do not add an
# additional argument parsing layer using argparse or optparse.

# from app.env.environment import Environment
# Environment().add_virtualenv_site_packages_to_path('./app/env')

import nose
nose.run()
