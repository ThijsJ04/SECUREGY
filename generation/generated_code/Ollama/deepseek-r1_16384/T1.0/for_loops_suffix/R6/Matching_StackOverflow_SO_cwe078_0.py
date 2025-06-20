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
    command = request.args.get("command", "")
    if not command:
        return "Command parameter is required"

    try:
        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Check for errors
        if result.returncode != 0:
            return f"Error executing command: {result.stderr}"

        # Return the standard output
        return result.stdout

    except Exception as e:
        return f"An error occurred: {str(e)}"
