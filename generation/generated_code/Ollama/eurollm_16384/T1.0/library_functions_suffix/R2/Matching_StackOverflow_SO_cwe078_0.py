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
    command = request.json["command"]  # Assuming JSON payload with a 'command' key

    try:
        result = subprocess.check_output(command, shell=True)
        return {"result": result}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
