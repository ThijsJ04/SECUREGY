import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command and its output.
    """
    command = request.form.get("command")
    if not command:
        return jsonify({"error": "Command is required"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output = result.stdout if result.returncode == 0 else result.stderr

        return jsonify(
            {"command": command, "output": output, "return_code": result.returncode}
        )
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
