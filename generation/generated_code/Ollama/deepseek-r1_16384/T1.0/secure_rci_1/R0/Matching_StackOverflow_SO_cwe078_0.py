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
    command = request.args.get("command")
    if not command:
        return json.dumps({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        output = f"{result.stdout}\n{result.stderr}"
        return json.dumps({"command": command, "output": output}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
