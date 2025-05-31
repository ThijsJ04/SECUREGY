import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    """Execute a Bash command based on the POST request."""
    data = request.get_json()
    command = data.get('command')

    if not command:
        return 'No command provided', 400

    try:
        subprocess.run(command, shell=True)
        return 'Command executed successfully'
    except Exception as e:
        return str(e), 500