import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form['command']  # Get the command from the POST request
    result = subprocess.run([command], shell=True, capture_output=True)
    return 'Command: {}\nError: {}'.format(command, result.stderr)