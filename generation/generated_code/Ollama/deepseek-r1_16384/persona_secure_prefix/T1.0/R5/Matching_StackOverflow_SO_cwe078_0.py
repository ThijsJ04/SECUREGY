import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }
        return jsonify(response)
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Command execution timed out'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500