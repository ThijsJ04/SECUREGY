@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if not 'command' in data:
        return {'message': 'No command provided'}
    command = data['command']
    output = subprocess.check_output(command, shell=True)
    return {'output': output.decode('utf-8')}