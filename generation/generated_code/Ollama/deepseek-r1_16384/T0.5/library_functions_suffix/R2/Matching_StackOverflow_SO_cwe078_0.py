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
    command = request.args.get("command")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        output = {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }

        return jsonify(output)

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
