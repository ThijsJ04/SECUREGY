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

    try:
        # Use subprocess.run to execute the command
        result = subprocess.run(
            ['bash', '-c', command],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        response = f"Command: {command}\nOutput: {result.stdout}"
        return jsonify({'message': 'Command executed successfully', 'output': response})

    except subprocess.CalledProcessError as e:
        app.logger.error(f"Command failed with error: {e.stderr}")
        return jsonify({'error': 'Command execution failed', 'details': e.stderr}), 500

    except Exception as e:
        app.logger.error(f"Unexpected error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500