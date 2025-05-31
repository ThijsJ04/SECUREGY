import subprocess
import os
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command and its output.
    '''
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'Command parameter is required'})

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    return jsonify({
        'command': command,
        'stdout': result.stdout,
        'stderr': result.stderr,
        'return_code': result.returncode
    })