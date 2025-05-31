import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.form.get('command')
    if not command:
        return "No command provided", 400
    result = subprocess.check_output(command, shell=True)
    return result.decode()