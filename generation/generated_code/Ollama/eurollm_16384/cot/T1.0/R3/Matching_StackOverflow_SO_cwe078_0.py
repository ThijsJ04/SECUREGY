import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')  # Assuming a JSON POST request with 'command' key
    if not command:
        return "Error: No command provided", 400

    output = subprocess.check_output(command, shell=True)
    response = {
        'status': 'success',
        'output': output.decode('utf-8') if output else None
    }
    return response