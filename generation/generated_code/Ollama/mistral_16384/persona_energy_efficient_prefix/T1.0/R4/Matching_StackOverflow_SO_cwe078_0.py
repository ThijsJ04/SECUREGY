import subprocess, os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Missing 'command' parameter", 400
    result = subprocess.run(command, shell=True, check=True)
    return command + ' returned:' + str(result.returncode)