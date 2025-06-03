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
    cmd = request.args.get("command")
    if not cmd:
        return "No command provided"

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        return f"Command: {cmd}\nOutput: {output}\nError: {error}"
    except Exception as e:
        return f"Error executing command: {str(e)}"
