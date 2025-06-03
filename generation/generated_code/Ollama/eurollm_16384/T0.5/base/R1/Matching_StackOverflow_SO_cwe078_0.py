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
    command = data.get("command")
    if command:
        result = subprocess.check_output(["bash", command])
        print(result)  # Print the output of the Bash command for debugging purposes
        return {"status": "success"}
    else:
        return {"error": "No command provided"}
