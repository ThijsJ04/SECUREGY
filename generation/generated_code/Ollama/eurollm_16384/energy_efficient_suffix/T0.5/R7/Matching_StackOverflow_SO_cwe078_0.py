import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body
    command = data['command']

    if not command:
        return {"error": "Command cannot be empty."}, 400

    result = subprocess.run(command, shell=True, capture_output=True)  # Run the bash command with shell=True to capture output
    stdout, stderr = result.stdout, result.stderr

    return {'stdout': stdout.decode('utf-8'), 'stderr': stderr.decode('utf-8')}, 200  # Return the output of the command