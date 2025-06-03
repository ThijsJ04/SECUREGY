import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")
    if not command:
        return "No command provided."

    try:
        subprocess.run(command, shell=True)
        return f"Command executed successfully: {command}"
    except Exception as e:
        return f"Error executing command: {e}"
