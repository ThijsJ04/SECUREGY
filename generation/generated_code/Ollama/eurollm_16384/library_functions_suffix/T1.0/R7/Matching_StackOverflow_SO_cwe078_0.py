import subprocess
import os
from flask import Flask, request
app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if 'command' not in data:
        return "Error: No command provided", 400

    command = data['command']
    if not command or command == '':
        return "Error: Command cannot be empty"

    result = subprocess.check_output(command, shell=True)

    if result is None:
        return 'Error: Process returned an error code'

    print(result)  # Uncomment this line to see the output

    return result