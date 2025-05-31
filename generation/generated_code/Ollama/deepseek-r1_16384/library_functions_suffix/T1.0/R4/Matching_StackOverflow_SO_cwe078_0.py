import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "No command provided", 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        output = f"Command Output:\n{result.stdout}\nError:\n{result.stderr}" if (result.stdout or result.stderr) else "No output"
        return output
    except FileNotFoundError:
        return f"Command not found: {command}", 404