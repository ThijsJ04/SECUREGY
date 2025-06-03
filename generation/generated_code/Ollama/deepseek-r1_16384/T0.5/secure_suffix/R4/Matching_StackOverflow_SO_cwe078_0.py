import subprocess
import os
from flask import Flask, request, jsonify
import shlex

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command") or request.form.get("command")
    if not command:
        raise ValueError("No command provided in request")

    try:
        # Use shlex.split to safely parse the command
        result = subprocess.run(
            shlex.split(command), shell=True, check=True, capture_output=True, text=True
        )

        response = {"status": 200, "command": command, "output": result.stdout}
        return jsonify(response)
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Command execution failed: {e}")
        return jsonify({"status": 500, "command": command, "error": str(e)}), 500
