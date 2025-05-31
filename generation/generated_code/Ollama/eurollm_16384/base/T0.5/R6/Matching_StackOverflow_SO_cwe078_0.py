import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    if not 'command' in request.form:
        return "Missing required parameter", 400
    command = request.form['command']
    result = subprocess.check_output(command, shell=True)
    return result.decode('utf-8')