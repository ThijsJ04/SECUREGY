import subprocess
import os
import json

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command") or request.form.get("command")

    if not command:
        return json.dumps({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output = result.stdout
        error = result.stderr

        if result.returncode != 0:
            return json.dumps({"command": command, "error": error}), 200

        return json.dumps({"command": command, "output": output}), 200

    except Exception as e:
        return json.dumps({"error": str(e)}), 500
