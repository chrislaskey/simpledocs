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


import glob, os, sys


absolute_path = os.path.abspath(__file__)
project_dir = os.path.dirname(absolute_path)
project_name = os.path.basename(project_dir)
project_name = 'simpledocs'
virtualenv = '/usr/lib/virtualenvs/{0}'.format(project_name)
site_packages = glob.glob('{0}/lib/*/site-packages'.format(virtualenv))[0]

sys.path.insert(0, project_dir)
sys.path.insert(0, site_packages)


from app import app as application


import nose
nose.run()
