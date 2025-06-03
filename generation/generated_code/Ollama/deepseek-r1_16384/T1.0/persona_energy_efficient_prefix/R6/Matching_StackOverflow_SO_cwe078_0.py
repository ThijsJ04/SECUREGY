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
    if "command" not in request.args:
        return "Error: No command provided", 400

    cmd = request.args["command"]

    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=10
        )

        if result.stderr:
            return f"Error: {result.stderr}\nOutput: {result.stdout}", 500

        return result.stdout, 200

    except subprocess.TimeoutExpired:
        return "Command timed out after 10 seconds", 408
    except Exception as e:
        return f"Unexpected error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
