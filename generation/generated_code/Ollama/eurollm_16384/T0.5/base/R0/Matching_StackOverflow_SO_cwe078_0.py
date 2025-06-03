import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form["command"]  # Get the bash command from the request
    if not os.path.exists("/tmp"):
        os.mkdir("/tmp")  # Create /tmp directory if it doesn't exist
        subprocess.check_call(
            [
                "bash",
                "-c",
                f'echo "Created /tmp directory" > /tmp/created_directory.txt',
            ]
        )
    else:
        with open("/tmp/created_directory.txt", "w") as file:
            file.write(
                "Created /tmp directory"
            )  # Write a message to the file if the directory already exists
    subprocess.check_call(command)
    return f"Bash command executed successfully: {command}"
