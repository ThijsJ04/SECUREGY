import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command and its output or error message in JSON format.

    Parameters:
        command (str): The bash command to execute, passed via query parameters.

    Returns:
        JSON object containing:
            - original_command: str
            - success: bool
            - output: str (stdout or stderr)
    """
    try:
        command = request.args.get("command")
        if not command:
            return jsonify({"error": "No command provided"}), 400

        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        output = result.stdout
        error = result.stderr
        success = result.returncode == 0

        response = {
            "original_command": command,
            "success": success,
            "output": output if success else error,
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
