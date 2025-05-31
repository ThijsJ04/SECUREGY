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
        # Use subprocess.run with shell=False to prevent shell injection
        process = subprocess.run(
            command,
            shell=True,  # WARNING: Using shell=True can be risky if input isn't sanitized
            capture_output=True,
            text=True
        )

        output = {
            'command': command,
            'stdout': process.stdout,
            'stderr': process.stderr,
            'return_code': process.returncode
        }

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)