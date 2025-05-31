import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')  # Assuming the command is sent in a POST request with a form field named 'command'
    if not command:
        return 'Command is required', 400

    # Execute the bash command
    output = subprocess.check_output(['bash', '-c', command])
    status = subprocess.wait([command])  # Wait for the command to finish executing

    return output, 200