from subprocess import run, PIPE

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', None)

    if not command:
        return {'error': 'Missing command parameter.'}, 400

    try:
        result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
        output = result.stdout.decode('utf-8')
        error = result.stderr.decode('utf-8')

        if error:
            return {'error': f'Error executing command: {error}'}, 400

        return {'command': command, 'output': output}
    except Exception as e:
        return {'error': f'An error occurred while executing the command. Details: {str(e)}'}, 500