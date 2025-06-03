import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command", "")
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if process.returncode == 0:
            return jsonify({"output": process.stdout}), 200
        else:
            error_message = f"Error: {process.stderr}"
            return jsonify({"error": error_message}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
