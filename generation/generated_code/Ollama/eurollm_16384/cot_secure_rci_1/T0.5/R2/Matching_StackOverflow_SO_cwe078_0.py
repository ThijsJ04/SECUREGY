import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')
    if not command:
        return 'No command provided.'

    # Check if the command is a valid bash command
    if not subprocess.call(["sh", "-c", command]):
        return 'Failed to execute command.'

    return f'Command executed successfully: {command}'