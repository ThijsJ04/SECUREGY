import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command")  # Get the command from the URL query string
    if not command:
        return "Error: No command provided."

    result = subprocess.check_output(command, shell=True)
    return result.decode()
