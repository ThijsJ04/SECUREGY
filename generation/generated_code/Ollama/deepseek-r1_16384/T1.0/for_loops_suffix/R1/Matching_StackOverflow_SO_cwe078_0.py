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

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=10
        )

        output = f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"

        return jsonify(
            {
                "command": command,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "return_code": result.returncode,
            }
        )

    except subprocess.TimeoutError:
        return jsonify({"error": "Command timed out"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
