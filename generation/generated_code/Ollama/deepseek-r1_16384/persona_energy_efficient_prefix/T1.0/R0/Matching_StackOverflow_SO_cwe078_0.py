import subprocess
import os
from flask import Flask, request, jsonify
from flask.wrappers import Response

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        if result.returncode == 0:
            return jsonify({
                'command': command,
                'output': result.stdout
            }), 200

        return jsonify({
            'error': f'Command failed: {result.stderr}',
            'command': command
        }), 500

    except Exception as e:
        return jsonify({
            'error': str(e),
            'command': command
        }), 500

if __name__ == '__main__':
    app.run(debug=True)