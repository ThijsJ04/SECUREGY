import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return jsonify({"error": "No command provided"}), 400
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )
        return jsonify(
            {
                "command": command,
                "output": result.stdout,
                "exit_code": result.returncode,
            }
        )
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e), "stderr": e.stderr}), 500
