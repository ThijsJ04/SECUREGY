import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash', methods=['GET', 'POST'])
def execute_bash():
    command = request.values.get('command')
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    error = result.stderr
    return jsonify({
        'command': command,
        'stdout': output,
        'stderr': error,
        'exit_code': result.returncode
    })