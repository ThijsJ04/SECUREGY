import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    """
    Take the bash command from the POST request and execute it using subprocess.
    Return the output of the executed command.
    """
    data = request.get_json()
    if not 'command' in data:
        return "Error: No command provided", 400
    cmd = data['command']
    result = os.system(cmd)
    return result, 200