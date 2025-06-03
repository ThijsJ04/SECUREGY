import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return "Error: No command provided", 400
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            return f"Error executing command: {result.stderr}", 500
        else:
            return f"Command executed successfully. Output: {result.stdout}", 200
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}", 500
