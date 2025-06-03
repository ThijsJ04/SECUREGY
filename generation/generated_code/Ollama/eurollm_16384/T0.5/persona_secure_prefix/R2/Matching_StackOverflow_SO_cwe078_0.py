import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", None)  # Get the bash command from the request
    if command is not None:  # If a command was provided, execute it
        try:
            output = subprocess.check_output(command, shell=True).decode("utf-8")
            return "Executed '{}' and output: {}".format(command, output)
        except Exception as e:  # Handle any exceptions that occur during execution
            return str(e)
    else:  # If no command was provided, return an error message
        return "No command provided"
