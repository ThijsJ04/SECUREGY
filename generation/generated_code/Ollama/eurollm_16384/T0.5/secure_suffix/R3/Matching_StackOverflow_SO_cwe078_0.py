import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()
    if not data:
        return "No JSON provided", 400

    command = data["command"]
    if not isinstance(command, str) or command == "":
        return "Invalid command", 400

    # Execute the Bash command and capture its output.
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    return {"output": output}
