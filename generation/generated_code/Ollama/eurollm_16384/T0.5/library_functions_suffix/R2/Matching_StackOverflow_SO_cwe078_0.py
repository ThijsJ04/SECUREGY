import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form["command"]
    result = subprocess.check_output(command, shell=True).decode()
    return f"Command executed: {command}"
