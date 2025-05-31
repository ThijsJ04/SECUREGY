@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if not 'command' in data:
        return "Error: No command provided."
    command = data['command']

    # Execute the bash command
    result = subprocess.check_output(command, shell=True)

    # Return the command as a JSON response
    return {'command': command}