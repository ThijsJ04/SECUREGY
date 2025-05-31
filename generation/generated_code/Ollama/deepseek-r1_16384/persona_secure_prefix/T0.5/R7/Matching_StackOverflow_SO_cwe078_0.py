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
    # Retrieve the command parameter from the request
    command = request.args.get('command', '')

    # Execute the command in a shell environment
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Capture both stdout and stderr outputs
    output = result.stdout.strip() if result.stdout else ''
    error = result.stderr.strip() if result.stderr else ''

    # Return the executed command along with its output or error message
    return f"Command: {command}\nOutput: {output}\nError: {error}"