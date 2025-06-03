import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Error: No command provided."

    output, error = subprocess.run(["bash", "-c", command], capture_output=True)
    if error:
        return f"Error executing command: {error}"
    else:
        return f"Command executed successfully:\n{output}"
