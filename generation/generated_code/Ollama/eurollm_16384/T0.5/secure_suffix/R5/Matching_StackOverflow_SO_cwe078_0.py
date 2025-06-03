import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    try:
        command = request.args.get("command")
        if not isinstance(command, str):
            return "Error: Invalid command", 400
        result = subprocess.run([command], shell=True, capture_output=True)
        return result.stdout
    except Exception as e:
        return f"Error: {str(e)}", 500
