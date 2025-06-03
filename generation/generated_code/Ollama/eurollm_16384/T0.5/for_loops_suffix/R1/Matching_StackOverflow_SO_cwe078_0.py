import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "No command provided", 400

    # Execute the bash command and return its output or error
    output = subprocess.check_output(command, shell=True)
    return output.decode()
