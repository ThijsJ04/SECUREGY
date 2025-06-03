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
    command = request.args.get("command", "")
    if not command:
        return "No command provided"

    try:
        output = subprocess.check_output(command, shell=True).decode()
        return f"Command executed: {output}"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
