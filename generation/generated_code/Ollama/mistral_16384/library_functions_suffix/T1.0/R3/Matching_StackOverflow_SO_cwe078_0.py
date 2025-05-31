from subprocess import check_output

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = check_output(command, shell=True)
    return command + ' -> ' + str(result)