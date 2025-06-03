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
    command = request.args.get("command")
    if command is None:
        return "Error: No command provided"
    else:
        try:
            subprocess.check_call(command, shell=True)
            return f"Command executed successfully: {command}"
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e}"
