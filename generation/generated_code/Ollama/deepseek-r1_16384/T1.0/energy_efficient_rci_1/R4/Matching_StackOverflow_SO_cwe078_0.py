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
    command = request.args.get("command")  # Get command parameter from query string
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        # Execute the command using subprocess.run
        result = subprocess.run(
            command,
            shell=True,  # Use shell to execute the command
            stdout=subprocess.PIPE,  # Capture stdout
            stderr=subprocess.PIPE,  # Capture stderr
        )

        # Get the output and return it
        response = {
            "command": command,
            "stdout": result.stdout.decode("utf-8"),
            "stderr": result.stderr.decode("utf-8"),
        }
        return jsonify(response)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
