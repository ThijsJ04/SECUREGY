import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")
    if not command:
        return "Command is required", 400

    # Execute the command
    try:
        subprocess.run(command, shell=True)
        return f"Command executed successfully: {command}"
    except subprocess.CalledProcessError as e:
        return f"Command execution failed with error code {e.returncode}: {e}", 500


if __name__ == "__main__":
    app.run(debug=True)
