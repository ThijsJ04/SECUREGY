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
    cmd = request.args.get("command", "")
    if not cmd:
        return "No command provided", 400
    try:
        result = subprocess.run(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output = result.stdout or ""
        error = result.stderr or ""
        response = f"Command: {cmd}\nOutput: {output}\nError: {error}"
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
