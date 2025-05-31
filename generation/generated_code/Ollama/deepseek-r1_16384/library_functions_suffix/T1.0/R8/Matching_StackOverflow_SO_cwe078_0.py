import subprocess
import os
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')
    if not command:
        return make_response(
            jsonify({'error': 'Command parameter is required'}), 400
        )

    try:
        result = subprocess.run(
            [f"/bin/bash", "-c", f"{command}"],
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        return jsonify({
            'status': 'success',
            'message': 'Command executed successfully',
            'output': result.stdout
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            'status': 'error',
            'message': f'Command execution failed: {str(e)}',
            'error_output': e.stderr
        }), 500