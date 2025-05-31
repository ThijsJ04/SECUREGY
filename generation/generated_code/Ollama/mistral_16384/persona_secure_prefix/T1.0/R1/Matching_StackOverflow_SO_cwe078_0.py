from subprocess import check_output, CalledProcessError

@app.route('/execute_bash')
def execute_bash():
    try:
        command = request.args.get('command')
        output = check_output([command], shell=True, universal_newlines=True)
    except CalledProcessError as e:
        return str(e), 1
    else:
        return command + " -> " + output