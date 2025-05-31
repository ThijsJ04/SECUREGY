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
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Run the command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        output = f"Standard Output: {result.stdout}\nStandard Error: {result.stderr}"
        success = result.returncode == 0

        return jsonify({
            'command_executed': command,
            'output': output,
            'success': success
        }), 200 if success else 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500