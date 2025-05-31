@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    command = data['command']
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return {'message': f"Command '{command}' executed successfully."}