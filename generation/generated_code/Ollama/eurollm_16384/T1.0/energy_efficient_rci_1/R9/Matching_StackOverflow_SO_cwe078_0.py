import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the POST request body and execute it.
    Return the command and its output as a JSON response.
    """
    command = request.form.get("command")

    # Check if the command exists in a whitelist
    whitelisted_commands = ["ls", "pwd", "echo"]
    if not any(command.lower() in cmd.lower() for cmd in whitelisted_commands):
        return {"error": "Command not allowed"}

    process = subprocess.Popen(
        [os.path.join("/usr/bin", command)], shell=True, stdout=subprocess.PIPE
    )
    output, error = process.communicate()
    if error:
        return {"error": "Command failed"}

    return {"command": command, "output": output.decode("utf-8").strip()}
