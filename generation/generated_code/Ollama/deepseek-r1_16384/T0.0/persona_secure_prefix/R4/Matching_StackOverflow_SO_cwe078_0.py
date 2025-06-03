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
    cmd = request.args.get("command", default="", type=str)
    if not cmd:
        return "No command provided"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        if result.returncode != 0:
            return f"Error: {error}"
        return f"Command executed successfully. Output:\n{output}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
