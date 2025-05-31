@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    for key, value in data.items():
        if key == 'command':
            try:
                output = subprocess.check_output(value, shell=True).decode('utf-8')
                return {'result': output}
            except subprocess.CalledProcessError as e:
                print(f"Bash command failed with error code: {e.returncode}")
                return {'error': f"Command '{value}' returned an error."}, 500
        elif key == 'args':
            args = value
    return {'error': "Invalid input data. Expected 'command' and 'args' keys in JSON payload."}, 400