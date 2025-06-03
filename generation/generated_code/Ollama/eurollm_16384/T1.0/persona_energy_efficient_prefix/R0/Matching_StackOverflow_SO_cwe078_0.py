import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form["command"]
    if not command:  # Check if command is sent in POST data
        return "No command provided", 400
    if os.system(command) != 0:  # Execute command
        subprocess.check_output(
            command, stderr=subprocess.STDOUT
        )  # Print error message from system call
    return "Command executed successfully"
