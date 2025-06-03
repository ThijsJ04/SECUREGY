import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    command = data.get("command")
    if not command:
        return "No command provided", 400

    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        return f"Command failed with exit code {result.returncode}", 500

    return command, 200
