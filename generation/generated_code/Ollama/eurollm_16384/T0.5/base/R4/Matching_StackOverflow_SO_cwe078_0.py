import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if "command" not in data or "output" not in data:
        return "Error: Missing command or output in JSON payload", 400

    command = data["command"]
    output = subprocess.check_output(command, shell=True)

    response = {"status": "success", "output": output}
    return response
