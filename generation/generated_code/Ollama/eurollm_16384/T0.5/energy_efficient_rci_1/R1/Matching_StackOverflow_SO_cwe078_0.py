import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    """
    Executes a Bash command given in the URL.
    """
    command = request.args.get("command")
    if not command:
        return "Error: No command provided."
    try:
        subprocess.check_call(
            command, shell=True
        )  # Execute the command using subprocess.check_call()
        return f"Command executed successfully: {command}"
    except subprocess.CalledProcessError as e:
        return f"Command execution failed with error: {e}. Command was: {command}"
