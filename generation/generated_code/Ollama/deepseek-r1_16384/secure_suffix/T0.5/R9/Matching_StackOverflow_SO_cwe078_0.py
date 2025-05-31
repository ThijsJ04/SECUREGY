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
        return jsonify({'message': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True, 
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = f"Command: {command}\nExit code: {result.returncode}\nOutput: {result.stdout}\nError: {result.stderr}"
        return jsonify({'message': 'Command executed successfully', 'output': output})

    except Exception as e:
        return jsonify({'message': f'Error executing command: {str(e)}'}), 500