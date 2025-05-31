from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if command is None:
        return "Error: No command provided.", 400

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOMESSED)
    except Exception as e:
        return str(e), 500

    return command + " -> " + str(output), 200