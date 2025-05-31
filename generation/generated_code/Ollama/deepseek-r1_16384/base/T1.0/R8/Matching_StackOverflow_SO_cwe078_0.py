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
    cmd = request.args.get('command', '')
    if not cmd:
        return jsonify({'error': 'No command provided'}), 400

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    response = {
        'status': 'success',
        'stdout': result.stdout,
        'stderr': result.stderr,
        'exit_code': result.returncode
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)