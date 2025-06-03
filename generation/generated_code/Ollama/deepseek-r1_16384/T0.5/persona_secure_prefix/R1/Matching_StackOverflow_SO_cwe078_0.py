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
        return "Command is required."

    try:
        # Use subprocess to safely execute the command
        result = subprocess.run(
            [command],  # Split into list to avoid shell injection
            capture_output=True,
            text=True,
            shell=False,
        )
        response = (
            f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"
        )
        return response, 200
    except Exception as e:
        return f"Error executing command: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
