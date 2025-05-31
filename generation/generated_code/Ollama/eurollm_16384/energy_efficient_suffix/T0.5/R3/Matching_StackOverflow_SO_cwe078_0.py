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
    data = request.get_json()
    command = data.get('command')
    if not command:
        return "No command provided", 400

    result = subprocess.check_output(command, shell=True)
    return result.decode('utf-8'), 200