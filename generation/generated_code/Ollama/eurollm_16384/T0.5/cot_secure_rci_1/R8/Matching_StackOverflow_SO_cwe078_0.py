import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")
    if not command:
        return "Error: No command provided."

    # Execute the bash command
    try:
        process = subprocess.run(
            [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        output = process.stdout.decode() if process.returncode == 0 else ""
        error = process.stderr.decode() if process.returncode != 0 else ""

        # Return the bash command to the client
        print(f"Bash Command: {command}")  # Print the command for logging purposes
        return f"Command executed successfully."
    except Exception as e:
        error = str(e)
        return f"Error executing bash command: {error}"
