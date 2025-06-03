import subprocess, os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    result = subprocess.check_output(command, shell=True)
    return {"command": command, "result": result.decode()}
