from subprocess import check_output, CalledProcessError

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command or an error message if execution fails.
    '''
    try:
        command = request.args.get('command', '')
        output = check_output([command], shell=True, universal_newlines=True)
        return command + ' --> ' + output
    except CalledProcessError as e:
        return command + ' failed with error: ' + str(e)