import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if not data or "command" not in data:
        return "Error: No command provided", 400

    command = data["command"]
    result = subprocess.check_output(command, shell=True)
    return {
        "message": "Command executed successfully."
        if result.stdout
        else "Failed to execute command.",
        "command": command,
    }
