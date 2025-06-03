import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "No command provided in JSON payload", 400

    try:
        subprocess.check_call(command)
        return f"Bash command executed successfully: {command}", 200
    except subprocess.CalledProcessError as e:
        return f"Bash command failed with error code: {e}", 500
