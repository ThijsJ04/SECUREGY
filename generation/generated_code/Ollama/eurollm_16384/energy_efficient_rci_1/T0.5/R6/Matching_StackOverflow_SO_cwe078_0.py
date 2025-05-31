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
        return "Error: Command is empty", 400

    try:
        subprocess.run(command, shell=True)
        return f"Command executed successfully: {command}"
    except Exception as e:
        return str(e), 500