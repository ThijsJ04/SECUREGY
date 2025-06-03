import subprocess, os, base64
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return {"error": "Command not found"}

    try:
        result = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOERRORIFEXITCODEISNOTZERO
        )
    except Exception as e:
        return {"error": str(e)}

    return {"command": command, "result": base64.b64encode(result).decode()}
