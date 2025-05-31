@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    os.system(command)  # Execute the command
    return command     # Return the command for response consistency