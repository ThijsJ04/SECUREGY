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
    if not data or "command" not in data:
        return {"error": "Missing required field: command"}, 400
    command = data["command"]
    result = subprocess.check_output(command, shell=True).decode("utf-8")
    return result
