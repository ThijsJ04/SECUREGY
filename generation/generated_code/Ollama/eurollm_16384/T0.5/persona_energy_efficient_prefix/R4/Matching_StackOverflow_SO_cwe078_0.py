import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")
    if not command:
        return "Command is empty!"

    # Execute the bash command using subprocess
    try:
        process = subprocess.Popen(["sh", "-c", command], stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return f"Error executing command: {error}"
    except Exception as e:
        return f"Failed to execute command: {str(e)}"

    # Return the bash command
    return "Command executed successfully!"
