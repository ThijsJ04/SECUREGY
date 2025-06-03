import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args["command"]  # Extract the bash command from the request
    try:
        output, error = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        print(
            f"Command output: {output.stdout}"
        )  # Print the command output for debugging purposes
        return f"Executing bash command: '{command}'"  # Return the original command
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}:")
        print(f"Error message: {error.stderr}")
        return f"Error executing bash command: '{command}' - Error code: {e.returncode}, Error message: {error.stderr}"  # Return an error message if the command fails
