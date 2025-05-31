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
    command = request.args.get('command')
    if not command:
        return "Command parameter is required", 400
    try:
        subprocess.run(command, shell=True)
        return f"Executed: {command}"
    except Exception as e:
        return f"Error executing command: {str(e)}", 500