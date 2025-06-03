import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return {"error": "Missing 'command' parameter."}, 400

    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"command": command, "result": result}
