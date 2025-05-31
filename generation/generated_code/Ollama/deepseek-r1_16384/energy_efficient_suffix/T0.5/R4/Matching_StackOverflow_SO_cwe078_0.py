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

    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        output = result.stdout
        error = result.stderr
        return_code = result.returncode

        if return_code != 0 and error:
            return jsonify({
                'command': command,
                'error': error
            }), 500

        return jsonify({
            'command': command,
            'output': output
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)