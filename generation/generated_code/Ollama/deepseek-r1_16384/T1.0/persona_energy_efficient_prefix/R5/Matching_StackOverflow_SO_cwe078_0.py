import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output.
    """
    if "command" in request.args:
        cmd = request.args["command"]
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return f"Command: {cmd}\nOutput: {result.stdout}"
        except subprocess.CalledProcessError as e:
            return f"Command execution failed. Error: {str(e)}"
    else:
        return "No command provided."


if __name__ == "__main__":
    app.run(debug=False)
