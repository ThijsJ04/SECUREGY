@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if not data or 'command' not in data:
        return {"error": "Invalid request"}, 400

    command = data['command']
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    response = {'status': 'success', 'output': output}

    return response