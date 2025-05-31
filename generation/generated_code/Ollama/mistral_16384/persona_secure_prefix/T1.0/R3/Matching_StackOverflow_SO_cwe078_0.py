from subprocess import Popen, PIPE

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = result.communicate()
    return {'output': output.decode(), 'error': error.decode()}