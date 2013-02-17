import subprocess

class CommandLine:

    def execute(self, command, stdin=None, stdout=None, stderr=None,
                return_boolean=False):
        '''
        Execute a command on the system. Return stdout on success, raise an
        exception on failure, and log result in either case. If return_boolean
        is True, return the boolean value based on system exit code (zero:True,
        non-zero:False) and do not log any results.
        '''
        # Verify passed arguments
        if not type(command) is list or len(command) == 0:
            raise Exception('Execute method received invalid command argument. '
                            'Should receive a list containing each command '
                            'token as a string. Instead received: '
                            '"{0}"'.format(command))

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
        else:
            raise Exception('Stdout: {0} | Stderr: {1}'.format(stdout, stderr))

    def execute_queue(self, commands, return_boolean=False):
        '''
        Execute multiple piped commands on the system. The argument commands
        should be a list containing a sublist for each command. The order of the
        list determines the order of the command: commands[0] | commands[1] |
        [...] | commands[n-1] | commands[n].
        Return stdout on success, raise an exception on failure, and log result
        in either case. If return_boolean is True, return the boolean value
        based on system exit code (zero:True, non-zero:False) and do not log
        any results.
        '''
        # Verify passed arguments
        if not type(commands) is list or len(commands) == 0:
            raise Exception('Execute queue method received invalid commands '
                            'argument. Should receive a list containing a '
                            'sublist for each command. Instead received: '
                            '"{0}"'.format(commands))

        # Create process pipes
        previous_command = None
        for command in commands:
            named_args = {'stdout':subprocess.PIPE, 'stderr':subprocess.PIPE}
            if previous_command:
                named_args['stdin'] = previous_command.stdout
            previous_command = subprocess.Popen(command, **named_args)

        # Set post process variables
        stdout, stderr = previous_command.communicate()
        is_success = (previous_command.returncode == 0)

        # Return a boolean if requested
        if return_boolean:
            return is_success

        # Otherwise return stdout on success and raise an error on failure.
        if is_success:
            return stdout
        else:
            raise Exception('Stdout: {0} | Stderr: {1}'.format(stdout, stderr))


if __name__ == "__main__":
    raise Exception("Library functions only, no direct access")
