import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Command not provided"

    # Execute the bash command and capture output
    result = subprocess.run(
        args=command,
        shell=True,
        text=True,
        capture_output=True
    )

    # Return stdout or stderr based on success
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error: {result.stderr}"