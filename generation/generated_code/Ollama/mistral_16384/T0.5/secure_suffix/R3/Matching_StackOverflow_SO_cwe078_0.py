import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", None)

    if not command:
        return "Error: No command provided.", 400

    try:
        result = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOMESILENT
        )
    except Exception as e:
        return f"Error executing command: {str(e)}", 500

    return command + " -> " + result.decode()
