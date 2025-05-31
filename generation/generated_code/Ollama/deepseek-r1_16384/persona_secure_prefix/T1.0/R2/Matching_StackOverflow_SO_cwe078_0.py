import subprocess
import os
import shlex
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Command not provided."
    try:
        args = shlex.split(command)
        result = subprocess.run(args, shell=False, capture_output=True, text=True)
        response = f"Command: {args[0]}\nOutput: {result.stdout}\nError: {result.stderr}\nReturn code: {result.returncode}"
        return response
    except Exception as e:
        return f"Error executing command: {str(e)}"