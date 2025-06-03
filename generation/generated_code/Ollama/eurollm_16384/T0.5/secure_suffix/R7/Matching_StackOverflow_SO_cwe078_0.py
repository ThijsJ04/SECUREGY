import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    if "command" not in request.args:
        return "Error: No command provided."
    try:
        process = subprocess.Popen(
            request.args["command"], stdout=subprocess.PIPE, shell=True
        )
        stdout, stderr = process.communicate()
        if stderr:
            return f"Error executing command '{request.args['command']}': {stderr.decode('utf-8')}"
        return request.args["command"] + "\n" + stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Error executing command '{request.args['command']}': {e}"
