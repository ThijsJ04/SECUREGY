import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


# Run 'ls' and print its output in the browser
@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    body = request.get_json()
    command = body.get("command")
    if not command:
        command = ""
    p = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    return {"output": p.stdout.decode("utf-8")}
