import json
import os
import sys

class Environment:

    ''' Handles options related to the python execution environment such as
    the adding of a virtualenv's site-packages directory. '''

    def add_virtualenv_site_packages_to_path(self, site_packages_path=""):
        site_packages_path = self._get_site_packages_path()
        if os.path.exists(site_packages_path):
            sys.path.insert(0, site_packages_path)

    def _get_site_packages_path(self):
        field = u'site_packages_path'
        site_packages_path = self._get_field_from_environment_data_file(field)
        if not site_packages_path:
            site_packages_path = self._get_best_guess_for_site_packages_path()
        return site_packages_path

    def _get_field_from_environment_data_file(self, field):
        base_path = os.getcwd()
        environment_file_path = '{0}/environment.json'.format(base_path)
        with open(environment_file_path) as file:
            raw_data = file.read()
            data = json.loads(raw_data)
            return data.get(field, None)

    def _get_best_guess_for_site_packages_path(self):
        base_path = os.getcwd()
        virtualenv_dir = self._get_best_guess_for_virtualenv_dir()
        python_version = self._get_python_version_string()
        path = '{0}/{1}/lib/{2}/site-packages'.format(
            base_path, virtualenv_dir, python_version
        )
        return path

    def _get_best_guess_for_virtualenv_dir(self):
        base_path = os.getcwd()
        exists = os.path.exists
        possible_dirs = [
            '.venv', 'venv', 'env', 'virtualenv', '.virtualenv',
            '.config/virtualenv', '.meta/virtualenv'
        ]
        for dir in possible_dirs:
            full_path = '{0}/{1}'.format(base_path, dir)
            if exists(full_path):
                return dir
        raise Exception('Could not guess virtualenv dir, please specify a '
                        '"site_packages_path" argument.')

    def _get_python_version_string(self):
        major = sys.version_info[0]
        minor = sys.version_info[1]
        python_version = 'python{0}.{1}'.format(major, minor)
        return python_version

