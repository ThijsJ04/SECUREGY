import subprocess
import os
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """

    command = request.args.get("command")
    if not command:
        return "No command provided"

    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if result.returncode == 0:
            response = Response(result.stdout, content_type="text/plain")
        else:
            response = Response(f"Error: {result.stderr}", content_type="text/plain")

        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"
