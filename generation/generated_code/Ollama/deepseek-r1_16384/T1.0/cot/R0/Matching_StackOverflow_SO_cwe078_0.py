import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command's output or an error message if something goes wrong.
    """
    command = request.args.get("command")

    if not command:
        return "Command parameter is required", 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            error_message = result.stderr
            return f"Error executing command: {error_message}", 400

        output = result.stdout
        return output, 200

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500
