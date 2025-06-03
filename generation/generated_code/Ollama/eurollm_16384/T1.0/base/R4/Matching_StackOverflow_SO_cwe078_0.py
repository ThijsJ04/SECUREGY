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
    try:
        # Ensure there is a single command in the request body
        command = request.json["command"]

        if not os.system(f"echo {command} && {command} > /dev/null &;") == 0:
            return "Error executing bash command."
    except ValueError as e:
        # Handle cases where the request doesn't contain a 'command' field or it is invalid.
        abort(400, description="Invalid JSON response")
    return command  # Return the command to prevent abuse.
