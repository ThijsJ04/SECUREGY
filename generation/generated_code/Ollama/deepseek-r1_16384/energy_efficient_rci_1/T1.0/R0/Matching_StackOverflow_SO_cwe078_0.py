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
    command = request.form.get('command')
    if not command:
        return "Command parameter is missing."
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        return f"Error executing command: {str(e)}"
    return command