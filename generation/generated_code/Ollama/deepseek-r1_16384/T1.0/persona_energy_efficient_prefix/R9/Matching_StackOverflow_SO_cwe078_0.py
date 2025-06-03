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
    # Get the command parameter from the request
    command = request.args.get("command")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        # Execute the bash command using subprocess.run
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=False
        )

        # Return the command and its output as JSON
        return jsonify(
            {
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
            }
        ), 200

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
