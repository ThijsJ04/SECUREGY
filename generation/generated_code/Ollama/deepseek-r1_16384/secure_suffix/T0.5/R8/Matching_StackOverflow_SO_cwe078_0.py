import subprocess
import os
import shlex
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        result = subprocess.run(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        output = result.stdout.decode('utf-8', errors='ignore')
        error = result.stderr.decode('utf-8', errors='ignore')

        response = {'command': command}
        if output:
            response['output'] = output
        elif error:
            response['error'] = error

        return jsonify(response)
    except subprocess.TimeoutExpired as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': f'Command execution failed: {str(e)}'}), 500