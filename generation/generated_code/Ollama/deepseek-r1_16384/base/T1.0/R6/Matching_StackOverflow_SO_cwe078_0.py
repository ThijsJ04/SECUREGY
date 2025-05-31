import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output.
    '''
    command = request.args.get('command', '')
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        output = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }

        if result.returncode != 0:
            return jsonify(output), 500

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)