import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", default=None)
    if command is not None and "#!" in command:  # check if the input has a shebang
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        return "Output: " + p.stdout.read()
    else:  # if the input does not have a shebang or is not valid
        os.system(command)
        return "Executed command: " + command
