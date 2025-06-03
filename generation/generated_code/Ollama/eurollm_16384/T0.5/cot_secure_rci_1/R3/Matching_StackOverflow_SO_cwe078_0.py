import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "No command provided in the request", 400

    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout
