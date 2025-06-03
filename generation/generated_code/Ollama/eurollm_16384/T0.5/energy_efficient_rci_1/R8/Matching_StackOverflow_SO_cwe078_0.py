import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form[
        "command"
    ]  # Assuming the command is in a POST request with key 'command'
    result = subprocess.check_output(command, shell=True)
    return result.decode("utf-8")
