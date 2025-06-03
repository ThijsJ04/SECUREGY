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
    command = request.json.get(
        "command"
    )  # Assuming JSON data is sent in the request body
    if not command:
        return "Error: No command provided", 400

    try:
        subprocess.check_call(command, shell=True)
        return f"Command '{command}' executed successfully."
    except subprocess.CalledProcessError as e:
        return (
            f"Command '{command}' failed with error code {e.returncode}.\nError message: {str(e)}",
            500,
        )
