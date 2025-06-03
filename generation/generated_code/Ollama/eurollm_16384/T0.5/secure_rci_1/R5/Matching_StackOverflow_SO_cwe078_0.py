import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    for key, value in data.items():
        if key == "command":
            subprocess.run(value)
            return value
