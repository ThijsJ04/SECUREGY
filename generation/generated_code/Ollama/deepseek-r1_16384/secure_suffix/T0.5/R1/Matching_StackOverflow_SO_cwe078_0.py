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
    if 'command' not in request.args:
        return jsonify({'error': 'No command provided'}), 400

    command = request.args['command']

    try:
        result = subprocess.run(
            command,
            shell=True,  # Using shell is necessary to split the command into arguments
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        return jsonify({
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }), 200

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)