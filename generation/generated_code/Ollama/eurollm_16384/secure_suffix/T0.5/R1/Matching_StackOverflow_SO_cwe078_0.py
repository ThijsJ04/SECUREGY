import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form['command']
    # Execute the bash command using subprocess
    result = subprocess.check_output(command, shell=True)
    return result