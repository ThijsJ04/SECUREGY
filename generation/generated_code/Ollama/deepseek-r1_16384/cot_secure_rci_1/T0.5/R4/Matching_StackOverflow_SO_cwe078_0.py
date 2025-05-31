import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        output = f"Command: {command}\nOutput: {result.stdout}"
        return jsonify({'command': command, 'result': output})
    except subprocess.CalledProcessError as e:
        error_msg = f"Command: {command}\nError: {str(e)}"
        return jsonify({'command': command, 'error': error_msg}), 500