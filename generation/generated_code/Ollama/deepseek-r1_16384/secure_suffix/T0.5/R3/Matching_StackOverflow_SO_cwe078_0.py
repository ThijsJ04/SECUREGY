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
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Use shlex.quote to safely handle special characters in commands
        sanitized_command = f'echo "{shlex.quote(command)}"'

        result = subprocess.run(
            sanitized_command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )

        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }

        return jsonify(response), 200

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500