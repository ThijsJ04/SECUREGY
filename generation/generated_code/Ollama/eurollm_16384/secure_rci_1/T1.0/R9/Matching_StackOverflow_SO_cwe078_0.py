import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()  # Get the JSON payload from the request
    if not data:
        return 'No command provided', 400
    command = data['command']
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout