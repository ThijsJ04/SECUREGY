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
    data = request.get_json()  # Assuming JSON input
    command = data.get('command')  # Assuming only one key 'command'
    if not command:
        return {"error": "No command provided"}
    result = subprocess.run(command, shell=True, capture_output=True)
    output = result.stdout.decode('utf-8')  # Convert bytes to string
    return {'result': output}