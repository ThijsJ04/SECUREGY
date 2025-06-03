import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if command is None:
        return "Missing required key: command", 400

    # Execute the bash command using subprocess.run() and return the output
    output = subprocess.run(command, shell=True, capture_output=True)
    status = output.returncode
    if status != 0:
        return "Command failed with error code {}".format(status), 500

    # Return the command as JSON response
    return {"command": command}, 200
