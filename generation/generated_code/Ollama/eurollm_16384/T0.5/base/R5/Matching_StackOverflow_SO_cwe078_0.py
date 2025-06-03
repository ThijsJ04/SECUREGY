import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if "command" not in data:
        return "Error: Missing command", 400

    command = data["command"]
    result = subprocess.run(command, shell=True, capture_output=True)

    # Check if the command was successful
    if result.returncode == 0:
        return f"Command executed successfully: {command}"
    else:
        return f"Error executing command: {result.stderr.decode('utf-8')}"
