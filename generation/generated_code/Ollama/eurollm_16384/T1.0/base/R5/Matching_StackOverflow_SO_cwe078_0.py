import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

# ... (previous imports and app definition remain unchanged)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    if "command" not in request.json or not isinstance(request.json["command"], str):
        return "Invalid JSON", 400

    command = request.json["command"]
    # Validate the Bash command using a library like `subprocess`
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if not os.path.exists("temp_file"):
        os.remove("temp_file")  # Remove temporary file if it exists
    with open("temp_file", "wb") as f:
        f.write(stdout)
    try:
        with open("temp_file", "r") as f:
            stdout = f.read()
        process = subprocess.Popen(
            ["bash", "-c"],
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        _, _, stderr = process.communicate(input="true")
    except FileNotFoundError:
        pass
    try:
        with open("temp_file", "wb") as f:
            f.write(stderr.decode())
    finally:
        os.remove("temp_file")  # Remove temporary file in case of error

    if stderr is not None and len(stderr) > 0:
        return stderr, 500

    response = {"command": command}
    return response
