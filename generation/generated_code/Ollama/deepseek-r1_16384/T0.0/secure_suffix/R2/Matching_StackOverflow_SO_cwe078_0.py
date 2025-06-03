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

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
        )

        output = f"Command: {command}\nOutput: {result.stdout}"

        if result.returncode != 0:
            output += f"\nError: {result.stderr}"

        return jsonify({"command": command, "output": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
