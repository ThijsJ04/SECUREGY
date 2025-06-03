import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Command parameter is missing", 400
    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = f"Command: {command}\nOutput: {result.stdout if result.stdout else ''}\nError: {result.stderr if result.stderr else ''}"
        return output, 200
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}", 500
