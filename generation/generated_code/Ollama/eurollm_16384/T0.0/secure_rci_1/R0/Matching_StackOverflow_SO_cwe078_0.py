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
    command = data.get("command")
    if not command:
        return "Error: No command provided", 400

    # Execute the Bash command
    result = subprocess.run(["bash", "-c", command], capture_output=True, text=True)
    stdout, stderr = result.stdout, result.stderr

    if not os.path.exists("/tmp"):
        os.mkdir("/tmp")

    # Save the output to a temporary file
    with open(f"/tmp/output_{command}.txt", "w") as f:
        f.write(stdout)
        f.write(stderr)

    return "Command executed successfully", 200
