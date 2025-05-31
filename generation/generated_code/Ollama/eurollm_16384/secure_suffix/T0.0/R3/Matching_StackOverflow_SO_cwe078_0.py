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
        return "Error: No command provided", 400

    # Execute the Bash command
    result = subprocess.run(['bash', '-c'], input=command, shell=True)
    stdout, stderr = result.stdout, result.stderr

    if result.returncode != 0:
        return f"Error executing command: {result.stderr}", 500

    # Return the executed command as JSON
    return {'command': command}, 200