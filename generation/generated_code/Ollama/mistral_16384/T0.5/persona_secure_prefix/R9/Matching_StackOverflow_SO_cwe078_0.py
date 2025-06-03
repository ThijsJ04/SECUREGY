import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", None)

    if not command:
        return "No command provided", 400

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOERR)
    except Exception as e:
        return str(e), 500

    return command + "\nOutput:\n" + output.decode("utf-8")
