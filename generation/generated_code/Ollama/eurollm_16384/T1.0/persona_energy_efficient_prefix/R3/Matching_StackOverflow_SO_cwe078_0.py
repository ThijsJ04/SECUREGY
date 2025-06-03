import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """Execute the bash command from the request."""
    try:
        # Check if the key exists in the request data
        command = request.json.get("command")
        if not command:
            return jsonify({"error": "Command is missing."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    try:
        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        stdout, stderr = process.communicate()
        output = str(stdout.decode("utf-8"))  # Decode the output to UTF-8
    except Exception as e:
        return jsonify({"error": "Failed to execute command."}), 500

    if stderr:
        err_message = str(stderr.decode("utf-8"))  # Decode the error message to UTF-8
        return jsonify({"error": err_message, "output": output})
    else:
        return jsonify({"output": output})
