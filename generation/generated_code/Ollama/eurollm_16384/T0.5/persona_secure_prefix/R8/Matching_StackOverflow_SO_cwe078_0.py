import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "No command provided", 400

    # Execute the bash command
    try:
        subprocess.check_call([command], shell=True)
        return f"Command executed successfully: {command}"
    except subprocess.CalledProcessError as e:
        return f"Command execution failed: {e}", 500
