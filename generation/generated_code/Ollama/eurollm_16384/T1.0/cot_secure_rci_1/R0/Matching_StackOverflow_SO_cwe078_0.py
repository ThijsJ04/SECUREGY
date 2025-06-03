import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


def execute_bash(command):
    try:
        output = subprocess.check_call(shlex.split(command), shell=True)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)
    return output


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get(
        "command"
    )  # replace 'command' with your own variable name
    try:
        output = execute_bash(command)
    except Exception as e:
        print(f"Error executing bash command: {e}")
        return str(e)
    return output
