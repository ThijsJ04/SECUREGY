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
    command = request.args.get("command", None)

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        output = f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}\nExit Code: {result.returncode}"

        return jsonify({"executed_command": command, "output": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
