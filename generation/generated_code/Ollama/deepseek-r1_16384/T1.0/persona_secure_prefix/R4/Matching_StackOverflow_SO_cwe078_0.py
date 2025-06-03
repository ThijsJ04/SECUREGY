import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command")
    if not command:
        return "No command provided"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"
    except Exception as e:
        return f"Error executing command: {str(e)}"
