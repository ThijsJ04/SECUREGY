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
        return jsonify({'error': 'Command is required'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        output = f"stdout: {result.stdout}\nstderr: {result.stderr}"

        if result.returncode == 0:
            return jsonify({'output': output}), 200
        else:
            return jsonify({'error': 'Command execution failed', 'output': output}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500