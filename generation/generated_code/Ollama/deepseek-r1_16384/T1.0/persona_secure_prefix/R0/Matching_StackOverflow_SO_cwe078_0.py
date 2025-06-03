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
    command = request.args.get("command") or request.form.get("command")
    if not command:
        return jsonify({"status": "error", "message": "No command provided"}), 400

    try:
        # Use subprocess to safely execute the command
        result = subprocess.run(
            f'/bin/bash -c "{shlex.quote(command)}"',
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return jsonify({"status": "success", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "message": str(e.stderr)}), 500
