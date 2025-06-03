import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form[
        "command"
    ]  # Assuming the command is passed in a form field named 'command'
    result = subprocess.run(
        command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return result.stdout  # Return the output of the bash command
