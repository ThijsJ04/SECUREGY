import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    try:
        # Get the command from the request and ensure it's a string
        command = str(request.args.get("command"))
    except KeyError:
        return "Error: No command provided", 400
    except Exception as e:
        return f"Error: {e}", 500

    try:
        # Execute the bash command using subprocess.run() and capture output
        process = subprocess.run(
            [command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
    except Exception as e:
        return f"Error executing command: {e}", 500

    # Return the command that was executed (or the error message if the command didn't execute successfully)
    if "command" in process.stdout:
        return f"Command executed:\n{process.stdout}\n", 200
    else:
        return "Error executing command", 500
