@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = subprocess.run(command, shell=True, stdout=subprocess.TEXT)
    return command + ' - output: ' + str(result.stdout)