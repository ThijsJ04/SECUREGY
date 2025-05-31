@app.route('/execute_bash', methods=['GET'])
def execute_bash():
    data = request.get_json()
    command = data.get('command')
    if not command:
        return 'Error: No command provided.'

    # Execute the bash command and get the output
    output = subprocess.check_output(command, shell=True)
    return output.decode()