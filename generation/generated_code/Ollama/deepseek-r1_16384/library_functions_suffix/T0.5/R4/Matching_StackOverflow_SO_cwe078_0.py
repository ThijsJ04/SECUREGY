import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400
    try:
        process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.stdout.decode()
        error = process.stderr.decode()
        result = {
            'command': command,
            'stdout': output if output else '',
            'stderr': error if error else '',
            'return_code': process.returncode
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500