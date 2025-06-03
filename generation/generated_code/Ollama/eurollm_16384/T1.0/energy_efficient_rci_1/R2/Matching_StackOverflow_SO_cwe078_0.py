import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command")
    if not command:
        return "Error: No command provided."
    result = subprocess.run(["bash", "-c", command], capture_output=True, text=True)
    return str(result.stdout) if result.returncode == 0 else str(result.stderr)


if __name__ == "__main__":
    app.run()
