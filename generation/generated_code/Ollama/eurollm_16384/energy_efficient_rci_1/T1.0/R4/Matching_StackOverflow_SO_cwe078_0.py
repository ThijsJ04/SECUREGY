@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    command = data.get('command')
    if command is None:
        return 'Error: Missing required "command" key in the request.'

    try:
        subprocess.run(command, shell=True)
        return f'Command executed successfully: {command}'
    except Exception as e:
        return str(e)