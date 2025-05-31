import subprocess
import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    if 'command' not in request.args:
        return jsonify({'error': 'No command provided'}), 400

    command = request.args.get('command')

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = f"Command: {command}\nOutput: {result.stdout if result.stdout else ''}"
        if result.stderr:
            output += f"\nError: {result.stderr}"

        return jsonify({'command': command, 'output': output}), 200

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500