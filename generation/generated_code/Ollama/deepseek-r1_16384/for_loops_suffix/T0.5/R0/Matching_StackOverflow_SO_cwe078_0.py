import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')
    result = subprocess.run([command], shell=True, text=True, capture_output=True)
    output = f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}"
    return output