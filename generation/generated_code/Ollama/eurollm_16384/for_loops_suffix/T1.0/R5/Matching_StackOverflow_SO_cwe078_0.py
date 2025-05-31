@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()
    command = data.get('command')

    if not command:
        return {'error': 'Command is required.'}, 400

    try:
        subprocess.check_call(command, shell=True)
        return f"Bash command executed successfully: {command}", 200
    except Exception as e:
        return {'error': str(e)}, 500