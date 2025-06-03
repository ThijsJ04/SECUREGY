from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Missing 'command' parameter", 400
    result = subprocess.check_output(
        command, shell=True, stderr=subprocess.STDOERRORFSPEC
    )
    return jsonify({"command": command, "result": result})
