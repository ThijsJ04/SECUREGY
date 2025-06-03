import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the POST request as JSON and execute it in a subprocess.
    Return the output of the executed command.
    """
    data = request.get_json()
    cmd = data["command"]
    try:
        process = subprocess.Popen(
            cmd, shell=True
        )  # Using shell=True is generally recommended for bash commands
        output = ""
        for line in iter(process.stdout.readline, b""):
            output += line
    except Exception as e:
        app.logger.error(f"Error executing command {cmd}: {e}")
        return "", 500

    return output.decode("utf-8"), 200  # Return the output of the executed command
