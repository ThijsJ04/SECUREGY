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
    command = request.args.get("command", "")
    if not command:
        return "No command provided", 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"
        return output
    except subprocess.CalledProcessError as e:
        return f"Command failed with error: {str(e)}", 500
