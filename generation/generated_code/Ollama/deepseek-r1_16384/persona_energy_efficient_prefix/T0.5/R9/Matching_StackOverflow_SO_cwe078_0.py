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
    command = request.args.get('command')

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )

        response = {
            'stdout': result.stdout,
            'stderr': result.stderr,
            'exit_code': result.returncode
        }
        return jsonify(response)

    except subprocess.CalledProcessError as e:
        error_response = {
            'error': str(e),
            'exit_code': e.returncode
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    app.run(debug=True)