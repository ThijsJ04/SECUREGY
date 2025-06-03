import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store the commands and their outputs
commands = {}


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON supplied"}), 400

    command = data["command"]

    # Execute the bash command and store the output in a dictionary
    output = subprocess.check_output(command, shell=True).decode("utf-8")

    if "error" not in commands:
        commands["error"] = []
    commands["error"].append({"command": command, "output": output})

    # Return the output of the last executed command
    if len(commands) > 0 and "error" not in commands:
        print(f"Last executed command: {command}")
        return jsonify({"output": commands["error"][-1]["output"]})
    else:
        return jsonify({"error": "No error message found"}), 204
