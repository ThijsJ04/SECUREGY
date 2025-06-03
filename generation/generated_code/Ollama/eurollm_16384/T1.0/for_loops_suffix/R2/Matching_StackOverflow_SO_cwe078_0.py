import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()
    if not data:
        return "Invalid JSON request"

    command = data.get("command")
    if not command or not isinstance(command, str):
        return "No valid bash command provided"

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output = process.stdout.read()
        return output
    except Exception as e:
        return f"Error executing bash command: {str(e)}"
