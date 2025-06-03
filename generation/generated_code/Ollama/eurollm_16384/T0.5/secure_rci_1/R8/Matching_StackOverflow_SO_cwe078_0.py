import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "Error: No command provided."

    result = subprocess.check_output(command, shell=True)
    return result.decode()
