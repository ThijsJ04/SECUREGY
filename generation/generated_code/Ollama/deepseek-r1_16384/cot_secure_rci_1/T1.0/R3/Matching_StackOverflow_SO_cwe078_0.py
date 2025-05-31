import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Inputs:
        - HTTP GET request with query parameter 'command'

    Outputs:
        - JSON object containing:
            {
                "command": string,
                "output": string,
                "error": string (if any)
            }
    '''
    try:
        command = request.args.get('command')

        if not command:
            return jsonify({'error': 'No command provided'}), 400

        # Execute the command using subprocess
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = f"Command: {command}\nOutput: {process.stdout if process.stdout else ''}"
        error = f"Error: {process.stderr if process.stderr else ''}"

        return jsonify({
            'command': command,
            'output': process.stdout,
            'error': process.stderr
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500