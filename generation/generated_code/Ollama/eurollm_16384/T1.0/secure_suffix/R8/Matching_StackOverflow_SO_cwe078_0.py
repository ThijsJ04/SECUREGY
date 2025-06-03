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
    if not "command" in data:
        return "No 'command' parameter found in JSON object"

    command = data["command"]
    if os.name == "nt":  # Check if platform is Windows
        print("Executing Command on Windows")
        subprocess.run(command, shell=True)
        return "Command executed successfully."
    else:  # Check if platform is not Windows
        print("Executing Command on Linux/MacOS")
        subprocess.check_call(command, shell=True)
        return "Command executed successfully."
