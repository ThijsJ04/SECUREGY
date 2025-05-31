@app.route('/execute_bash', methods=['GET'])
def execute_bash():
    """
    Executes a bash command from the request parameters.

    Args:
        None (as there are no arguments to pass)

    Returns:
        string: The bash command as a response
    """
    command = request.args.get('command')
    if command is None or not os.path.exists(os.path.dirname(__file__)) or not os.access(os.path.dirname(__file__), os.X_OK):
        return "Command does not exist"

    subprocess.check_call(command, shell=True)
    return command