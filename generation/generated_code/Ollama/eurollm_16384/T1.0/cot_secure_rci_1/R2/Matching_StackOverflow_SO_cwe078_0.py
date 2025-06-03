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
    command = request.form["command"]
    subprocess.run(["/bin/sh", "-c", command], check=False)
    return f"Command executed successfully: {command}"
