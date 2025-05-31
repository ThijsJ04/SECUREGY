@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if 'command' not in data:
        return 'Invalid request, missing command key', 400

    command = data['command']
    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        return f'Command failed with exit code {result.returncode}', 500

    return f'Bash command executed successfully: {result.stdout}'