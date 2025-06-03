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
    command = os.path.abspath(request.args.get("command", ""))

    if not os.path.exists(os.path.dirname(command)):
        return "Directory does not exist"

    try:
        subprocess.run(
            [command], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except Exception as e:
        return str(e)

    return "Command executed successfully"
