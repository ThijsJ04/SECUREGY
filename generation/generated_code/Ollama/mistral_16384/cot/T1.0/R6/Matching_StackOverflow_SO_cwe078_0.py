@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Missing 'command' parameter", 400
    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        return str(e), 500
    return command + "\n" + result