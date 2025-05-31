import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    if not command:
        return "Please provide a command"

    try:
        cmd = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
    except Exception as e:
        return f"Error: {str(e)}"

    output = cmd.stdout.strip()
    if output:
        return output
    else:
        return command