import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.form.get("command")
    if not command:
        return "Please provide a command to execute"
    try:
        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output, err = process.communicate()
        if output is None and err is not None:
            return "Bash command failed with an error"
        print(f"Command output:\n{output}")
        return f"Command stdout:\n{output}\nCommand stderr:\n{err}"
    except subprocess.CalledProcessError as e:
        return f"Bash command failed with an error: {e.strerror}"
