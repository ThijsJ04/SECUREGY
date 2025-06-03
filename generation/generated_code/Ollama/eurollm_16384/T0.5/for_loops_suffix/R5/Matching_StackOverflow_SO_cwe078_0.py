import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the POST request and execute it using subprocess.run().
    Return the output of the command as a string.
    """
    data = request.get_json()
    command = data["command"] if "command" in data else None
    if not command:
        return {"error": "No command provided"}

    try:
        process = subprocess.run(command, shell=True, capture_output=True)
        return process.stdout.decode("utf-8") if process.returncode == 0 else None
    except Exception as e:
        return {"error": str(e)}
