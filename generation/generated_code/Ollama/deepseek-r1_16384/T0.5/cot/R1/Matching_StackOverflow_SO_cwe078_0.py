import subprocess
import os
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    :return: The executed command and its output in JSON format
    """
    command = request.args.get("command", "")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

        return jsonify(
            {
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "success": True,
            }
        ), 200

    except subprocess.CalledProcessError as e:
        error_message = f"Command failed: {str(e)}"
        return jsonify({"error": error_message}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({"error": error_message}), 500
