import subprocess
import os
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')  # Get the command parameter from query string
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        # Execute the command with subprocess.run, capturing output and errors
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10  # Set a reasonable timeout
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

if __name__ == '__main__':
    app.run(debug=True)