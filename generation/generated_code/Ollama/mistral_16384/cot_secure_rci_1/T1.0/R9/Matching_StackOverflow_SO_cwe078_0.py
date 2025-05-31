from subprocess import check_output

...

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    result = check_output(command, shell=True, universal_newlines=True)
    return result