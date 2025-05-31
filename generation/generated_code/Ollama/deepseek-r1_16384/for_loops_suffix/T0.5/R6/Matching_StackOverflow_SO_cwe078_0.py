import subprocess
import os
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')

    if not command:
        return json.jsonify({'error': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        response = {
            'command': command,
            'output': result.stdout,
            'error': result.stderr if result.returncode != 0 else ''
        }

        return json.jsonify(response)

    except subprocess.SubprocessError as e:
        return json.jsonify({'error': str(e)}), 500