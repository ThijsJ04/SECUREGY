import subprocess, os
import flask
from flask import Flask

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return {"error": "No command provided"}
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        return {"error": str(e)}
    else:
        return {"command": command, "result": output}
