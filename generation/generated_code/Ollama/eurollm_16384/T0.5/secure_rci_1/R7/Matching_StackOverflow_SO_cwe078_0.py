import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """Executes a Bash command based on the input received through an API."""
    data = request.get_json()
    command = data.get("command")
    if not command:
        return "Error: Command is required", 400
    output = subprocess.check_output(command, shell=True)
    return output.decode("utf-8")
