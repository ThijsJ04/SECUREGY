import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()  # Assuming the request body contains JSON data
    command = data.get("command")
    if command:
        subprocess.run(command)
        return "Command executed successfully!"
    else:
        return "No command provided."


app.run(debug=True)
