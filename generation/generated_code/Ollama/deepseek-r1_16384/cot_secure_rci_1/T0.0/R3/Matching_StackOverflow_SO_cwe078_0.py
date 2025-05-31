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

    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return jsonify({
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr
        })

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500