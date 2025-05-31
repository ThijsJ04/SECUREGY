@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    os.system(command)  # execute the bash command in a separate process
    return {'command': command}  # return the executed command for confirmation