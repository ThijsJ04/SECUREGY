import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET", "POST"])
def execute_bash():
    command = request.args.get("command")
    result = subprocess.check_call(command, shell=True)
    return response.json(result)
