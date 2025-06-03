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
    data = request.get_json()  # Assuming the POST request comes with JSON data
    command = data["command"]  # Assuming the 'command' key is present in the JSON data

    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout + "\n"
