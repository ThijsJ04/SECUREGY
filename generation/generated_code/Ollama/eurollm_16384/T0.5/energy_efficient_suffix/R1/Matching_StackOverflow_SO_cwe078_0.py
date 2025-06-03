import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get("command")
    if not command:
        return "No command provided", 400

    # Execute the command
    result = subprocess.run(command, shell=True, capture_output=True)

    # Return the output of the command
    return {"result": result.stdout}
