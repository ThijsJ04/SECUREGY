import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "No command provided."
    try:
        subprocess.run(command, shell=True)
        return f"Command executed: {command}"
    except Exception as e:
        return f"Error executing command: {e}"
