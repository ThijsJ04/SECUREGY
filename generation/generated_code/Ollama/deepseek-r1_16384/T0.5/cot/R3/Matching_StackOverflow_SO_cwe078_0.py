import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    # Extract the command parameter from the request
    command = request.args.get("command") or request.form.get("command")

    if not command:
        return "No command provided"

    # Execute the bash command and capture output
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    # Return the captured output
    return result.stdout
