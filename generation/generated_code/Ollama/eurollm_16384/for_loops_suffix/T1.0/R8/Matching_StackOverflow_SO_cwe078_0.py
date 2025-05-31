import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')  # Get the shell command from the request
    result = subprocess.run(command, shell=True, capture_output=True)  # Execute the command
    return {"status": "ok" if result.returncode == 0 else "error", "command": command}