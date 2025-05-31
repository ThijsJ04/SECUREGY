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
        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            check=True,  # This will raise an error if command fails
            capture_output=True,  # Captures stdout and stderr
            text=True  # Returns strings instead of bytes
        )

        return jsonify({
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }), 200

    except subprocess.CalledProcessError as e:
        # If the command fails, capture the error message
        return jsonify({'error': str(e), 'command': command}), 500
    except Exception as e:
        # Handle other unexpected exceptions
        return jsonify({'error': str(e), 'command': command}), 500