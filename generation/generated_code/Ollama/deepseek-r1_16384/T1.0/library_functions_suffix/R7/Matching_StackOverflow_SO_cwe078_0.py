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
    command = request.args.get("command", "")
    if not command:
        return "Error: No command provided."
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        response = (
            f"Command: {command}\nOutput:\n{result.stdout}\n\nError:\n{result.stderr}"
        )
        return response
    except Exception as e:
        return f"Error executing command: {e}"


if __name__ == "__main__":
    app.run(debug=True)
