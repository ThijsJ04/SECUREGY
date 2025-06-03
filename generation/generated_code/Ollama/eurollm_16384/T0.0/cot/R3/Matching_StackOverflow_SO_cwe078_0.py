import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()  # Get the JSON data from the request
    if "command" not in data:
        return "Error: Missing command", 400

    command = data["command"]
    output = subprocess.run(f"bash -c '{command}'", capture_output=True, text=True)

    # Remove the newline character from the output string
    if output.stdout:
        output = output.stdout.rstrip("\n")

    return command
