import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "No command provided."

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        # Process the output here or return it as is
        return (
            "Command executed successfully."
            if not error
            else f"Error executing command: {error}"
        )
    except subprocess.CalledProcessError as e:
        return f"Command execution failed with code {e.returncode}: {e}."
