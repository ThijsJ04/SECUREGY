import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['GET'])
def execute_bash():
    command = request.args.get('command')
    if not command:  # ensure the command is present in the request
        return 'Error: No command provided'

    # Parse the command into individual elements (e.g., word, arguments, options) using shlex
    args = shlex.split(command)

    # Execute the command and handle errors
    try:
        process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:  # non-zero return code indicates an error
            raise Exception('Command execution failed')
    except Exception as e:
        print(f'Error executing command: {e}')
        return 'An error occurred'

    return command