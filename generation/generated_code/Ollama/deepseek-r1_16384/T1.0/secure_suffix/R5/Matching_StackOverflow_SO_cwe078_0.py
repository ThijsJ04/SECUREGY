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
        return "Error: No command provided"

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return f"Command executed successfully. Output: {result.stdout}"
        else:
            return f"Error occurred._stderr: {result.stderr}"

    except subprocess.CalledProcessError as e:
        return f"Command failed: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
