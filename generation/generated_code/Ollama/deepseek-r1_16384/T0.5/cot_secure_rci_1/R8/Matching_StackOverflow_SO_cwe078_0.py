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
    cmd = request.args.get("command")
    if not cmd:
        return jsonify({"error": "No command provided"}), 400

    try:
        process = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        output = {
            "command": cmd,
            "exit_code": process.returncode,
            "stdout": process.stdout,
            "stderr": process.stderr,
        }

        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
