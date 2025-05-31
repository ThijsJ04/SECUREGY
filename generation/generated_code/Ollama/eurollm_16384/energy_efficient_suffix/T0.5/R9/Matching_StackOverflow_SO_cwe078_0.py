@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')
    if not command:
        return 'Command is required', 400

    # Execute the bash command using subprocess.run()
    output = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Return the command and its output
    return {'command': command, 'stdout': output.stdout}