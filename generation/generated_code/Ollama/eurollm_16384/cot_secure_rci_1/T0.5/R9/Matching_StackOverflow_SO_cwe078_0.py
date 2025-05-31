@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    # Get the bash command from the request
    command = request.json.get('command')
    if not command:
        return {'error': 'No command provided'}