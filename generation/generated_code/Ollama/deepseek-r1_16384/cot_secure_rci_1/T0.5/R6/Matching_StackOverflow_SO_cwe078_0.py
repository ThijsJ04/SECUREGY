import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command and its output.
    '''
    command = request.args.get('command', '')

    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        # Execute the bash command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        output = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500