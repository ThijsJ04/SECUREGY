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
    if 'command' not in request.args:
        return jsonify({'error': 'Command parameter is missing'}), 400

    command = request.args['command']

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        response = {
            'success': result.returncode == 0,
            'command': command,
            'output': result.stdout if result.returncode == 0 else '',
            'error': result.stderr if result.returncode != 0 else ''
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500