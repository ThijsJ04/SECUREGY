import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", None)
    if not command:
        return jsonify({"error": "Command not provided"}), 400

    try:
        proc = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = proc.stdout
        error = proc.stderr
        return_code = proc.returncode

        result = {
            "command": command,
            "output": output,
            "error": error if error else "",
            "return_code": return_code,
        }

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
