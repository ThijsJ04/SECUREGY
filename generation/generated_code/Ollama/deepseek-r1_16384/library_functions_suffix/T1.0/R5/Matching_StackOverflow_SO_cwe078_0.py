from flask import Flask, request, jsonify
import subprocess
import os
import shlex

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
        # Use subprocess to run the command safely
        result = subprocess.run(
            shlex.quote(command),
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        return jsonify({
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500