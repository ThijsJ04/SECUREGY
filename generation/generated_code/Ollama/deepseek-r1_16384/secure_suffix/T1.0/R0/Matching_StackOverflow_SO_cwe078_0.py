import subprocess
import os
import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output.
    '''
    try:
        # Extract the command from GET or POST parameters
        command = request.args.get('command') if request.args else None
        if not command:
            return jsonify({'error': 'No command provided'}), 400

        # Execute the command safely using subprocess.run
        result = subprocess.run(
            command,
            shell=False,          # Avoid shell=True to prevent command injection
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True           # Raises CalledProcessError if command fails
        )

        return jsonify({'command': command, 'output': result.stdout}), 200

    except subprocess.CalledProcessError as e:
        logging.error(f"Command execution failed: {e}")
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({'error': 'Internal server error'}), 500