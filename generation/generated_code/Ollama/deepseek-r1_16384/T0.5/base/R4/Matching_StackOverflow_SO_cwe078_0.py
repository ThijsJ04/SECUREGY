import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command's output.
    """
    command = request.args.get("command")

    if not command:
        return jsonify({"error": "Command parameter is missing"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    output = result.stdout if result.returncode == 0 else result.stderr

    return jsonify({"command": command, "output": output})
