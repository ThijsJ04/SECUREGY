import subprocess
import os
from flask import Flask, request
from shlex import split

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '', type=str)
    if not command:
        return "Command parameter is missing"
    try:
        command_parts = split(command)  # Safely split the command
    except ValueError:
        return "Invalid command format"
    try:
        result = subprocess.run(
            command_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return f"Command executed successfully.\nOutput: {result.stdout}"
        else:
            return f"Command failed with error code {result.returncode}.\nError: {result.stderr}"
    except Exception as e:
        return f"An error occurred while executing the command: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)