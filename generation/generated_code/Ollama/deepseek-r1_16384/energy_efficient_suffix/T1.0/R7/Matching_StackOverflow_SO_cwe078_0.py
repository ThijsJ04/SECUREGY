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
    command = request.values.get('command', '')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            timeout=10
        )
        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({
            'command': command,
            'output': output,
            'return_code': result.returncode
        }), 200 if result.returncode == 0 else 500
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Command execution timeout'}), 408

if __name__ == '__main__':
    app.run(debug=True)