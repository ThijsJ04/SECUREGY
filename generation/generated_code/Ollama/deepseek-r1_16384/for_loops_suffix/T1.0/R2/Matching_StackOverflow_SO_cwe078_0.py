import subprocess
import os

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')

    if not command:
        return jsonify({'error': 'Command not provided'}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr or ''

        # Return a JSON response with the command and its execution results
        return jsonify({
            'command': command,
            'output': output,
            'error': error
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)