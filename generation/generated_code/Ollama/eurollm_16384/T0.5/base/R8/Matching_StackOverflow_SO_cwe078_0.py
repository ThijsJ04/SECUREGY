import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

# Set the maximum size of the command to execute (to prevent potential command injection attacks)
MAX_COMMAND_SIZE = 2048


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Execute a bash command from the request body.
    """
    data = request.get_json()
    if not "command" in data:
        return "Error: Missing required key 'command'"

    # Validate the command size (to prevent potential command injection attacks)
    command = data["command"]
    if len(command) > MAX_COMMAND_SIZE:
        return "Error: Command is too long. Maximum length is {} characters".format(
            MAX_COMMAND_SIZE
        )

    # Execute the bash command and return its output
    process = subprocess.Popen(
        [command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    output, error = process.communicate()

    if error:
        return "Error executing command: {}".format(error.decode())

    # Return the output of the bash command as a JSON response
    return {"result": output.decode()}
