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
    if "command" not in request.args:
        return jsonify({"error": "No command provided"}), 400
    cmd = request.args.get("command")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True)
        output = result.stdout.decode()
        error = result.stderr.decode()
        exit_code = result.returncode
        return jsonify(
            {"command": cmd, "stdout": output, "stderr": error, "exit_code": exit_code}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
