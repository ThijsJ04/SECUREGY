import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    os.system(command)  # Execute the command
    return command  # Return the command for response consistency
