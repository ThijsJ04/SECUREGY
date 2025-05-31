import subprocess, os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOERR)
    return command, output