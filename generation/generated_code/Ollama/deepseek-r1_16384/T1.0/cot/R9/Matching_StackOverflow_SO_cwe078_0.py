import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command and its output.
    """
    command = request.args.get("command", "")
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = f"Command: {command}\nOutput:\n{result.stdout or ''}\nError:\n{result.stderr or ''}"
        return jsonify({"command": command, "output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
