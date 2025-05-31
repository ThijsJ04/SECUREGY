import subprocess, os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        result = str(e)
    return f'Command: {command}\nResult: {result}'