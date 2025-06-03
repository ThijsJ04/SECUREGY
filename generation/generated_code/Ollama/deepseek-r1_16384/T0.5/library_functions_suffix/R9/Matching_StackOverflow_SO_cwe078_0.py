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
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output = f"{result.stdout}{result.stderr}"
        return jsonify({"command": command, "output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
