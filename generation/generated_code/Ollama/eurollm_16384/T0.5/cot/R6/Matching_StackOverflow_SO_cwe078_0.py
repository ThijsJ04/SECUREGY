import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.args.get("command")  # Extract the bash command from the request
    output = subprocess.check_output(
        command, shell=True
    )  # Execute the bash command and capture its output
    return output.decode()  # Return the output of the bash command as a response
