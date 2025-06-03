import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if not data or "command" not in data:
        return jsonify({"error": "Missing required key: command"}), 400

    command = data["command"]

    try:
        process = subprocess.Popen(command, shell=True)
        stdout, stderr = process.communicate()
        if stderr:
            return jsonify(
                {
                    "error": f"Error executing bash command '{command}': {stderr.decode('utf-8')}"
                }
            ), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Return the output of the Bash command if it succeeds
    try:
        content = stdout.decode("utf-8")
        return jsonify(content=content)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
