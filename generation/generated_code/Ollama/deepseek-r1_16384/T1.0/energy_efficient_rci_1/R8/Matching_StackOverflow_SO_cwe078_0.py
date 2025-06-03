import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return jsonify({"error": "Command parameter is required"}), 400
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = {
            "command": command,
            "exit_code": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
        return jsonify(output)
    except Exception as e:
        error_info = {"error": str(e), "message": "Command execution failed"}
        return jsonify(error_info), 500
