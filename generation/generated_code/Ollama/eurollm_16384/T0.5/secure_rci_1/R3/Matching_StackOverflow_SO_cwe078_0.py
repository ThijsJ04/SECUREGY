import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if "command" not in data:
        return "Error: Missing command parameter", 400

    command = data["command"]
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    return output
