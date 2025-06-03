import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()
    command = data.get("command")
    if command:
        try:
            # Execute the command in a subprocess
            process = subprocess.Popen(command, shell=True)
            output, error = process.communicate()
            return (
                {"status": "success", "message": output}
                if not error
                else {"status": "failure", "message": error}
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "invalid_request"}
