import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Error: Missing command argument", 400
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        return f"Error executing command: {str(e)}", 500
    return command + "\n\nOutput:\n" + output
