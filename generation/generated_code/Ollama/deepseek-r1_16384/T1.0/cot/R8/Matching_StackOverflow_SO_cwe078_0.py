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
    try:
        # Get command from request arguments
        command = request.args.get("command", "")

        if not command:
            return jsonify({"error": "No command provided"}), 400

        # Execute bash command
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        response = {
            "command": command,
            "stdout": result.stdout if result.stdout else "",
            "stderr": result.stderr if result.stderr else "",
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
