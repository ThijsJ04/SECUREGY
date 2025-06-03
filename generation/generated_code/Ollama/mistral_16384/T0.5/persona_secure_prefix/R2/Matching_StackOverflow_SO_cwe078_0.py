import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Missing 'command' parameter", 400

    result = subprocess.run(
        command, shell=True, stdout=subprocess.TEXT, stderr=subprocess.STDOUT
    )
    return result.stdout.decode()
