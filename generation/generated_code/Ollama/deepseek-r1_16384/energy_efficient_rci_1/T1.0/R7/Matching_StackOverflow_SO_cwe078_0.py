import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', default='', type=str)
    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400
    try:
        result = subprocess.run(command, shell=True, check=False, capture_output=True, text=True)
        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500