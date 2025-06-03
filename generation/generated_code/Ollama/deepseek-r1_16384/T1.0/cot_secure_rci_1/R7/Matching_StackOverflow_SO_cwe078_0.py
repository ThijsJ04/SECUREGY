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
    cmd = request.args.get("command", "")
    if not cmd:
        return jsonify({"error": "No command provided"}), 400
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        response = {
            "command": cmd,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
