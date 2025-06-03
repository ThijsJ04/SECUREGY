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
    try:
        command = request.json["command"]  # assuming the command is in JSON format
        if not isinstance(command, str) or not os.path.exists(command):
            raise ValueError("Invalid command")

        # execute the bash command and return it
        process = subprocess.Popen(
            [command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )  # execute with output redirected to standard output (no error output)
        output = ""
        while True:
            line = process.stdout.readline()
            if not line:
                break
            output += line.decode("utf-8")
        process.wait()  # wait for the command to finish executing

        return output, 200, {"ContentType": "text/plain"}
    except Exception as e:
        return str(e), 500, {"ContentType": "text/plain"}
