@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = subprocess.check_output(command, shell=True, universal_newlines=True)
    return command + '\n\n' + result