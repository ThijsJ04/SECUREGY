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
    try:
        command = request.form["command"]
        # Check if command is not empty
        if len(command) > 0:
            process = subprocess.Popen(
                ["/bin/bash", "-c", command],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
            )
            output, error = process.communicate()
    except KeyError:
        # Handle the case when there's no 'command' in the request
        pass
    except subprocess.CalledProcessError as e:
        # Handle the case when the command returns an exit code that indicates an error
        print(e)
        return f"Failed to execute command: {e}"
    else:
        # Return the command in the response
        return (
            "Executing command:" + output.decode()
            if len(output.decode()) > 0
            else f"Command not found or empty."
        )
