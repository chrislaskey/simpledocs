import os.path
import subprocess
from collections import defaultdict


def search_query(keywords):
    matches = _SearchResultsParser()._search_for_matches(keywords)
    success = _search_success(matches)
    results = {
        'keywords': keywords,
        'matches': matches,
        'success': success
    }
    return results

def _search_success(matches):
    return True if matches else False


class _SearchResultsParser:

    ''' Executes native file system search using Python subprocesses '''

    def _search_for_matches(self, terms):
        self.cli = CommandLine()
        self.results = defaultdict(int)
        for term in terms:
            self._search_file_names(term)
            self._search_file_contents(term)
        results_as_list = self._get_results_as_list()
        return results_as_list

    def _search_file_names(self, term):
        term = '*{0}*'.format(term)
        command = ['find', 'docs/', '-iname', term]
        options = {'raise_exception_on_failure': False}
        results = self.cli.execute(command, **options)
        self._compile_command_results(results, 3)

    def _search_file_contents(self, term):
        command = ['grep', '-l', '-r', '-i', term, 'docs/']
        options = {'raise_exception_on_failure': False}
        results = self.cli.execute(command, **options)
        self._compile_command_results(results)

    def _compile_command_results(self, results, weight=1):
        files = results.split('\n')
        filtered = [x for x in files if x]
        for file in filtered:
            file = os.path.normpath(file)
            # Using a defaultdict datatype to skip key/val instantiation
            self.results[file] += weight

    def _get_results_as_list(self):
        results_list = sorted(self.results, key=self.results.get, reverse=True)
        return results_list


class CommandLine:

    def execute(self, command, stdin=None, stdout=None, stderr=None,
                return_boolean=False, raise_exception_on_failure=True):
        '''
        Execute a command on the system. Return stdout on success, raise an
        exception on failure, and log result in either case. If return_boolean
        is True, return the boolean value based on system exit code (zero:True,
        non-zero:False) and do not log any results.
        '''
        # Verify passed arguments
        if not type(command) is list or len(command) == 0:
            raise Exception('Execute method received invalid command argument.'
                            ' Should receive a list containing each command'
                            ' token as a string. Instead received:'
                            ' "{0}"'.format(command))

        # Setup command
        named_args = { 'stdout':subprocess.PIPE, 'stderr':subprocess.PIPE }
        if stdin:
            named_args['stdin'] = stdin
        if stdout:
            named_args['stdout'] = stdout
        if stderr:
            named_args['stderr'] = stderr

        # Initiate process and listen for completion. Determine success from
        # return code
        process = subprocess.Popen(command, **named_args)
        stdout, stderr = process.communicate()
        is_success = (process.returncode == 0)

        # Return a boolean if requested
        if return_boolean:
            return is_success

        # Otherwise return stdout on success and raise an error on failure.
        if is_success:
            return stdout

        if raise_exception_on_failure:
            raise Exception('Stdout: {0} | Stderr: {1}'.format(stdout, stderr))
        else:
            return ''
