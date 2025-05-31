import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')  # Assuming the bash command is sent in JSON format
    if not command:
        return 'Invalid request', 400

    output = subprocess.check_output(command, shell=True)  # Execute the Bash command using subprocess
    print(output)  # You can modify this to return the output as a response instead of printing it

    return 'Bash command executed successfully', 200