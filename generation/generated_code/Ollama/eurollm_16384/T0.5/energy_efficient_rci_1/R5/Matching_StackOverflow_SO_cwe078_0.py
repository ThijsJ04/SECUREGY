import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.json.get(
        "command"
    )  # Assuming the input is a JSON object with 'command' key
    if not command:
        return "Error: No command provided", 400

    result = subprocess.check_output(command, shell=True)
    print(f"Result of executing {command}:")
    print(result)
    return result.decode("utf-8")  # Return the output as a string
