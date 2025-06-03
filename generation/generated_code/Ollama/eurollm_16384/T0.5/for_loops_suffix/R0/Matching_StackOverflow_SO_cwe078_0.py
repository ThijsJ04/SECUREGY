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
    data = request.get_json()
    command = data.get("command")
    if not command:
        return {"error": "No command provided"}

    # Execute the bash command using subprocess
    result = subprocess.run(["bash", "-c", command], capture_output=True, text=True)
    stdout, stderr = result.stdout, result.stderr

    # Check if the command was successful
    if not stdout and not stderr:
        return {"result": f"Command '{command}' executed successfully."}
    else:
        return {"result": f"Error executing command '{command}': {stderr}"}
