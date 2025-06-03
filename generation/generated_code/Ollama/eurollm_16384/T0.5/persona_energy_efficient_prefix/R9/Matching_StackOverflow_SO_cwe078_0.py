import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if "command" not in data or "your_bash_command" not in data["command"]:
        return "Invalid JSON", 400

    command = data["command"]
    result = subprocess.check_output(command)
    return result, 200
