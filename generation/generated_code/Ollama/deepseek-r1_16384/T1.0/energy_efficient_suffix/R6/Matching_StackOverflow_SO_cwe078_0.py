import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command", "").strip()
    if not command:
        return "No command provided."

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        output = result.stdout or ""
        if result.returncode != 0:
            output += f"\nCommand exited with code {result.returncode}"
        return output
    except FileNotFoundError as e:
        return f"Command not found: {str(e)}", 400
