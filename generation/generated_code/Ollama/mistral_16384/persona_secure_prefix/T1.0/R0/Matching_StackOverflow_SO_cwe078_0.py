import subprocess, os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "No command provided.", 400
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOERR)
    except Exception as e:
        return str(e), 500
    return command + "\n\nResult:\n" + result