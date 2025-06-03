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

    # Execute the command
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )

    response = {
        "command": command,
        "stdout": result.stdout if result.stdout else "",
        "stderr": result.stderr if result.stderr else "",
        "return_code": result.returncode,
    }

    return json.dumps(response)
