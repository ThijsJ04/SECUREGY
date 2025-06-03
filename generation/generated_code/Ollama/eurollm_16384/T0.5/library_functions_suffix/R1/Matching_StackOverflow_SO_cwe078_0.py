import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the POST request and execute it.
    Return the command as a JSON response.
    """
    data = request.get_json()
    command = data.get("command")

    if not command:
        return {"error": "No command provided"}

    result = subprocess.check_output(command, shell=True)
    return {"command": command, "result": result.decode("utf-8")}
