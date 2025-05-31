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
    command = request.args.get('command') or request.form.get('command')
    if not command:
        return jsonify({'status': 'error', 'message': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return jsonify({
            'status': 'success',
            'command': command,
            'output': result.stdout
        })

    except subprocess.SubprocessError as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)