import subprocess, os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if command:
        result = subprocess.run(command, shell=True, check=True)
        return {"command": command, "result": result.stdout}
    else:
        return {"error": "No command provided"}
