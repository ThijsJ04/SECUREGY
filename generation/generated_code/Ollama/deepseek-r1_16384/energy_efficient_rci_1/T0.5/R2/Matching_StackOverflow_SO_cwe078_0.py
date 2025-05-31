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
    # Get the command from query parameters or form data
    command = request.args.get('command') or request.form.get('command')

    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        # Execute the bash command
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        return jsonify({
            'success': True,
            'command': command,
            'output': result.stdout
        })

    except subprocess.CalledProcessError as e:
        return jsonify({
            'success': False,
            'error': f'Command failed: {str(e)}'
        }), 500