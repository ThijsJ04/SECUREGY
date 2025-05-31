import subprocess, os, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    # Ensure the command is a string and base64 encoded if needed
    if isinstance(command, bytes):
        command = base64.decodebytes(command).decode("utf-8")
    # Execute the command and get the output
    result = subprocess.check_output(command, shell=True, universal_newlines=True)
    # Return the original command with the output as a comment
    return f'Command: {command}\nOutput:\n{result}'