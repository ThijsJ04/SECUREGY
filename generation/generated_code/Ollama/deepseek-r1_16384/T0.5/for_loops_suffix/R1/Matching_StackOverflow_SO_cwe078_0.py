import subprocess
import os
from flask import Flask, request, json

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command", "")

    if not command:
        return json.jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output = f"Command: {command}\nExit Code: {result.returncode}\nOutput:\n{result.stdout or 'None'}\nError:\n{result.stderr or 'None'}"

        return json.jsonify(
            {"command": command, "output": result.stdout, "error": result.stderr}
        ), 200

    except subprocess.SubprocessError as e:
        return json.jsonify({"error": str(e)}), 500
