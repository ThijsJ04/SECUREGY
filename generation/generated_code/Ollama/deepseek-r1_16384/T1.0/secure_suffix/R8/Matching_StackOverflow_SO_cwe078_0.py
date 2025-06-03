import subprocess
import os
from flask import Flask, request, jsonify
import shlex

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    cmd = request.args.get("command", "")
    if not cmd:
        return jsonify({"error": "Command parameter is missing"}), 400

    try:
        args = shlex.split(cmd)
    except ValueError as e:
        return jsonify({"error": f"Invalid command: {str(e)}"}), 400

    try:
        result = subprocess.run(args, capture_output=True, text=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    else:
        response = {
            "command": cmd,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
        return jsonify(response)
