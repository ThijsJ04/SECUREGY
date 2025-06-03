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
    command = request.args.get("command", "")

    try:
        # Use subprocess.run with shell=True for executing bash commands
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10,  # Add a reasonable timeout to prevent long-running commands
        )

        # Return the output as a JSON response
        return jsonify(
            {
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
            }
        )

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Command timed out"}), 500

    except Exception as e:
        app.logger.error(f"Error executing command: {command}, Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
