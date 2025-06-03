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
    command = request.args.get("command")
    if not command:
        return "Command parameter is missing", 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        if result.returncode != 0:
            return f"Error executing command: {error}", 500
        else:
            return output
    except Exception as e:
        return f"An error occurred while executing the command: {str(e)}", 500
