import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()  # Get the JSON payload of the POST request
    command = data["command"]

    if not os.path.exists("/tmp") or not os.access("/tmp", os.W_OK):
        os.mkdir("/tmp")

    with open(os.path.join("/tmp", "exec.sh"), "w") as f:
        f.write(command)  # Write the command to a temporary file

    subprocess.run(["bash", os.path.join("/tmp", "exec.sh")], check=True, shell=False)
    os.remove(
        os.path.join("/tmp", "exec.sh")
    )  # Remove the temporary file after execution
    return jsonify({"command": command})
