import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Command parameter is missing", 400
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}\nReturn code: {result.returncode}"
    return output