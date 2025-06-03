import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "", str)
    if not command:
        return jsonify({"error": "Command parameter is required"}), 400

    try:
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )

        result = {
            "command": command,
            "stdout": process.stdout,
            "stderr": process.stderr,
            "return_code": process.returncode,
        }

        if process.returncode != 0:
            return jsonify(result), 500

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
