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
        return jsonify({"error": "Command is required"}), 400

    try:
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        result = {
            "command": command,
            "success": process.returncode == 0,
            "output": process.stdout if process.returncode == 0 else process.stderr,
        }

        return jsonify(result), 200 if process.returncode == 0 else 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
