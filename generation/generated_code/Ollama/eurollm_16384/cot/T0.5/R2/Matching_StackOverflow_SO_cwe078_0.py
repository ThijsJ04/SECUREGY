import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.args.get('command')
    if not command:
        return 'Command is required', 400

    output = subprocess.check_output(command, shell=True)
    return output