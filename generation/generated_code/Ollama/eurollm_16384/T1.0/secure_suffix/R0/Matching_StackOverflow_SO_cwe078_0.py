import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    params = request.args
    if "command" in params:
        command = params["command"]
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        return {"command": command}  # Return the command to the client
