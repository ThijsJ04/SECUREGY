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
    cmd = request.args.get('command', '')
    if not cmd:
        return "No command provided"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return f"Command: {cmd}\nOutput: {result.stdout}\nError: {result.stderr}\nExit Code: {result.returncode}"