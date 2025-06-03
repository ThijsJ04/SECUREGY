import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if not "command" in data:
        return "Error: Missing command key", 400
    command = data["command"]
    result = subprocess.run(command, shell=True)
    return {"output": result.stdout}
