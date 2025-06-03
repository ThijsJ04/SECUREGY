import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get(
        "command"
    )  # Assuming the bash command is provided as JSON data in the request body
    if not command:
        return "Error: No command provided", 400

    result = subprocess.check_output(command, shell=True)
    return result.decode()
