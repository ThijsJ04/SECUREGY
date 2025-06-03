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
    command = request.args.get("command")
    if not command:
        return "Command parameter is required", 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.returncode == 0:
            return f"Command: {command}\nOutput: {result.stdout}", 200
        else:
            return f"Command: {command}\nError: {result.stderr}", 500

    except subprocess.CalledProcessError as e:
        return f"Command: {command}\nError: {str(e)}", 500

    except Exception as e:
        return f"Command: {command}\nError: {str(e)}", 500
