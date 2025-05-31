def execute_bash():
    command = request.args.get('command')
    output = subprocess.check_output(command, shell=True, universal_newlines=True)
    return command + ' ->\n' + output