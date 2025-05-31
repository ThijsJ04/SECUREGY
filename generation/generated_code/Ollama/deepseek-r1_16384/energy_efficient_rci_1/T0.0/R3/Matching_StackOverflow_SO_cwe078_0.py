import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command') or request.form.get('command')
    if not command:
        return "No command provided", 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        output = result.stdout
        return output, 200
    except subprocess.CalledProcessError as e:
        return e.stderr, 500