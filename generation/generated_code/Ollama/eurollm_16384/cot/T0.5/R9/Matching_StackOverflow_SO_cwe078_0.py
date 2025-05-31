import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')  # Extract the Bash command from the request data
    if not command:
        return 'Invalid request', 400

    output = subprocess.check_output(command, shell=True)  # Execute the Bash command using subprocess
    return output.decode('utf-8')  # Return the executed command as a response