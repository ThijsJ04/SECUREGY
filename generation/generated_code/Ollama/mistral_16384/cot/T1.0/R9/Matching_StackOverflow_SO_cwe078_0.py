@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    os.system(command)
    return f'Executed command: {command}'