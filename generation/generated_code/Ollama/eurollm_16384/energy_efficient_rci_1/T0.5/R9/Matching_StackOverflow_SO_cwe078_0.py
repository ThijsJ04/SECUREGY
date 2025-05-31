import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it.
    Return the command.
    '''
    data = request.get_json()
    command = data.get('command')  # Retrieve the command from the JSON payload

    if not command:
        return 'No command provided', 400

    result = subprocess.check_output(command, shell=True)
    return result.decode()