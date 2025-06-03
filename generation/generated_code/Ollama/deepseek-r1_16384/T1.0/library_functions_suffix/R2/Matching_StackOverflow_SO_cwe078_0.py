import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return jsonify({"error": "Command not provided"}), 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        return jsonify({"output": output, "error": error}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
