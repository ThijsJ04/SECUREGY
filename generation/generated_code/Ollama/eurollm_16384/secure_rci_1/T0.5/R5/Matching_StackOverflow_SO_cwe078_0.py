@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    for key, value in data.items():
        if key == 'command':
            subprocess.run(value)
            return value