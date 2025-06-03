import subprocess
import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return jsonify({"error": "Command parameter is required"}), 400
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify(
        {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode,
        }
    )
