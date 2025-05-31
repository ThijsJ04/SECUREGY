@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Error: command parameter is required.", 400
    result = subprocess.check_output(command, shell=True)
    return f"Command executed successfully.\n{command}\n\nResult:\n{result}"