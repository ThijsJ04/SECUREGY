import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    if not command:
        return "Command parameter is required"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        return jsonify({
            'command': command,
            'stdout': output,
            'stderr': error,
            'return_code': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500