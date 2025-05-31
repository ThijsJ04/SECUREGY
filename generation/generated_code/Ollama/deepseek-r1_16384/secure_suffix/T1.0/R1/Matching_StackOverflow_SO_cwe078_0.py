import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output or an error message.
    '''

    command = request.args.get('command', '')

    if not command:
        return jsonify({'error': 'Command parameter is required'})

    try:
        result = subprocess.run(
            command,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True
        )

        if result.returncode == 0:
            return jsonify({'output': result.stdout})
        else:
            return jsonify({'error': f'Error executing command: {result.stderr}'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)