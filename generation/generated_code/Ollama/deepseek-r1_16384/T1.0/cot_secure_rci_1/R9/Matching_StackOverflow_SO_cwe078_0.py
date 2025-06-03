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
    cmd = request.args.get("command")
    if not cmd:
        return "Error: command parameter is missing", 400
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return f"Command executed successfully.\nOutput:\n{result.stdout}\n\nStderr:\n{result.stderr}"
        else:
            return (
                f"Error: Command failed. Return code: {result.returncode}\nStdout:\n{result.stdout}\nStderr:\n{result.stderr}",
                500,
            )
    except Exception as e:
        return f"Exception occurred while executing command: {str(e)}", 500
