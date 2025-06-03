import subprocess
import os
import json
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    if "command" in request.args:
        cmd = request.args["command"]
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        response_data = {
            "command": cmd,
            "output": result.stdout + result.stderr,
            "status": f"Command exited with code {result.returncode}",
        }
        return json.dumps(response_data)
    else:
        return json.dumps({"error": "No command provided"}), 400
