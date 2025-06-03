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

    if not data or "command" not in data:
        return {"error": "No command provided"}

    command = data["command"]

    if not isinstance(command, str) or not command:
        return {"error": "Invalid command"}

    try:
        subprocess.check_call(command, shell=True)
        return {
            "status": "success",
            "message": f"Command executed successfully: {command}",
        }
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}
