import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


def execute_bash(command):
    try:
        # Execute the command using subprocess.run()
        process = subprocess.run([command], shell=True, capture_output=True, text=True)
        return process.stdout
    except FileNotFoundError:
        return "Command not found"
    except Exception as e:
        return str(e)


@app.route("/execute_bash", methods=["POST"])
def execute_bash_handler():
    command = request.form["command"]
    result = execute_bash(command)
    return result
