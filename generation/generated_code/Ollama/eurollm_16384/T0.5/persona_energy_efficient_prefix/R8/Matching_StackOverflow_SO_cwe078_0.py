import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form["command"]  # Get the command from the form data
    if not command:
        return "Command is empty", 400

    try:
        subprocess.check_call(command, shell=True)
        return f"Bash command executed successfully: {command}"
    except subprocess.CalledProcessError as e:
        return f"Bash command failed with error code: {e}", 500
