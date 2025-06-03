import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return jsonify({"error": "Command is required"}), 400
    try:
        result = subprocess.run(
            command.split(), shell=False, capture_output=True, text=True
        )
        status = "success" if result.returncode == 0 else "failed"
        output = result.stdout or ""
        error = result.stderr or ""
        return jsonify(
            {"command": command, "status": status, "output": output, "error": error}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
