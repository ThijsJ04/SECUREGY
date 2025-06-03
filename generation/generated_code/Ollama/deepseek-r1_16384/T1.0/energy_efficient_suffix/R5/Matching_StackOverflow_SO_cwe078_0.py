import subprocess
import os
from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command", "")
    if not command:
        raise ValueError("Command parameter is required")

    try:
        # Run the command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False,  # To catch errors
        )

        response = {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }
        return json.dumps(response)
    except Exception as e:
        return (
            f"Error executing command: {str(e)}",
            400,
            {"Content-Type": "application/json"},
        )


# (The rest of the code remains unchanged as per the input)
