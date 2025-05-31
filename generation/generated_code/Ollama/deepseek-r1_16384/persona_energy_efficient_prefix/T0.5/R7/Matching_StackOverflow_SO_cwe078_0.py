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
    command = request.args.get('command', '')

    if not command:
        return jsonify({'error': 'No command provided'}), 400

    try:
        completed_process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )

        output = completed_process.stdout
        error = completed_process.stderr

        return jsonify({
            'command': command,
            'stdout': output,
            'stderr': error,
            'return_code': completed_process.returncode
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)