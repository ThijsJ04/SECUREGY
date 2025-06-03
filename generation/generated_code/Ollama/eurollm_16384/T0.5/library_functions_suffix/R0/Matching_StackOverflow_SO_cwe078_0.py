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
    if not command:
        return "No command provided", 400

    # Use subprocess to run the Bash command
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        return f"Error executing command: {error}", 500

    return output.decode("utf-8")
